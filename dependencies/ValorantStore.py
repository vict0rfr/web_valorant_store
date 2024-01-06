import pickle
from os import path, getcwd, remove, mkdir
from time import time
import cfscrape
import requests
from dependencies.ValorantStoreException import ValorantStoreException

class ValorantStore:
    __auth = {}

    def __init__(self, username: str, password: str, region: str = "eu", sess_path: str = None, proxy=None):
        self.__username = username
        self.__password = password
        self.__region = region
        self.__proxy = proxy
        self.__sess_path = sess_path if sess_path else getcwd()
        if not path.exists(self.__sess_path):
            mkdir(self.__sess_path)
        self.__auth_file = path.join(self.__sess_path, f"riot_auth_{self.__username}.pickle")
        self.__cookie_file = path.join(self.__sess_path, f"riot_cookie_{self.__username}.pickle")
        if path.isfile(self.__auth_file) and time() - path.getmtime(self.__auth_file) < 3600:
            try:
                with open(self.__auth_file, "rb") as auth:
                    self.__auth = pickle.load(auth)
            except Exception:
                remove(self.__auth_file)
                self.__login()
        else:
            self.__login()
        self.headers = {
            "X-Riot-Entitlements-JWT": self.__auth["entitlements_token"],
            "Authorization": "Bearer " + self.__auth["access_token"],
        }
        self.request = requests.session()

    @staticmethod
    def __get_access_token(url: str) -> str:
        return [i.split("=")[-1] for i in url.split("#", 1)[-1].split("&") if i.startswith("access_token" + "=")][0]

    @staticmethod
    def __skin_image(skin: str) -> str:
        return f"https://media.valorant-api.com/weaponskinlevels/{skin}/displayicon.png"

    @staticmethod
    def __buddy_image(buddy: str) -> str:
        return f"https://media.valorant-api.com/buddylevels/{buddy}/displayicon.png"

    @staticmethod
    def __card_image(card: str) -> str:
        return f"https://media.valorant-api.com/playercards/{card}/largeart.png"

    @staticmethod
    def __spray_image(spray: str) -> str:
        return f"https://media.valorant-api.com/sprays/{spray}/fulltransparenticon.png"

    @staticmethod
    def __bundle_image(bundle: str) -> str:
        return f"https://media.valorant-api.com/bundles/{bundle}/displayicon.png"

    @staticmethod
    def skin_info(skin: str) -> dict:
        response = requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{skin}")
        try:
            return response.json()["data"]
        except Exception:
            raise ValorantStoreException("skin_info", "request", response)

    @staticmethod
    def buddy_info(buddy: str) -> dict:
        response = requests.get(f"https://valorant-api.com/v1/buddies/levels/{buddy}")
        try:
            return response.json()["data"]
        except Exception:
            raise ValorantStoreException("buddy_info", "request", response)

    @staticmethod
    def card_info(card: str) -> dict:
        response = requests.get(f"https://valorant-api.com/v1/playercards/{card}")
        try:
            return response.json()["data"]
        except Exception:
            raise ValorantStoreException("card_info", "request", response)

    @staticmethod
    def spray_info(spray: str) -> dict:
        response = requests.get(f"https://valorant-api.com/v1/sprays/{spray}")
        try:
            return response.json()["data"]
        except Exception:
            raise ValorantStoreException("spray_info", "request", response)

    @staticmethod
    def bundle_info(bundle: str) -> dict:
        response = requests.get(f"https://valorant-api.com/v1/bundles/{bundle}")
        try:
            return response.json()["data"]
        except Exception:
            raise ValorantStoreException("skin info", "request", response)

    @property
    def region(self) -> str:
        return self.__region

    @property
    def username(self) -> str:
        return self.__username

    @property
    def auth(self) -> dict:
        return self.__auth

    @property
    def sess_path(self) -> str:
        return self.__sess_path

    @property
    def proxy(self) -> str:
        return self.__proxy

    @property
    def auth_file(self) -> str:
        return self.__auth_file

    @property
    def cookie_file(self) -> str:
        return self.__cookie_file

    def __login(self):
        scraper = cfscrape.create_scraper()
        if self.__proxy:
            scraper.proxies = {
                'http': self.__proxy,
                'https': self.__proxy,
            }
        if path.isfile(self.__cookie_file):
            try:
                with open(self.__cookie_file, "rb") as cookies:
                    scraper.cookies = pickle.load(cookies)
                login_response = scraper.get(
                    "https://auth.riotgames.com/authorize?redirect_uri=https%3A%2F%2Fplayvalorant.com%2Fopt_in&client_id"
                    "=play-valorant-web-prod&response_type=token%20id_token&nonce=1", allow_redirects=False, timeout=15)
                if login_response.status_code != 303 or login_response.headers.get("location").find(
                        "access_token") == -1:
                    remove(self.__cookie_file)
                    return self.__login()
                else:
                    self.__auth["access_token"] = self.__get_access_token(login_response.headers.get("location"))
            except Exception:
                remove(self.__cookie_file)
                return self.__login()
        else:
            cookie_response = scraper.post("https://auth.riotgames.com/api/v1/authorization", json={
                "client_id": "play-valorant-web-prod",
                "nonce": "1",
                "redirect_uri": "https://playvalorant.com/opt_in",
                "response_type": "token id_token"
            }, timeout=15)
            try:
                cookie = cookie_response.json()
            except Exception:
                raise ValorantStoreException("cookie", "request", cookie_response)
            if "type" not in cookie:
                raise ValorantStoreException("cookie", "request", cookie_response)
            elif cookie["type"] != "auth":
                raise ValorantStoreException("cookie", "type", cookie_response)
            else:
                login_response = scraper.put("https://auth.riotgames.com/api/v1/authorization", json={
                    "type": "auth",
                    "username": self.__username,
                    "password": self.__password,
                    "remember": True,
                    "language": "en_US"
                }, timeout=15)
                with open(self.__cookie_file, "wb") as cookies:
                    pickle.dump(scraper.cookies, cookies)
            try:
                login = login_response.json()
            except Exception:
                raise ValorantStoreException("access", "request", login_response)
            if "type" in login and login["type"] == "multifactor":
                raise ValorantStoreException("access", "multifactor", login_response)
            try:
                self.__auth["access_token"] = self.__get_access_token(login["response"]["parameters"]["uri"])
            except Exception:
                raise ValorantStoreException("access", "token", login_response)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.__auth["access_token"]
        }
        entitlements_response = scraper.post("https://entitlements.auth.riotgames.com/api/token/v1", headers=headers,
                                             timeout=15)
        try:
            entitlements = entitlements_response.json()
            self.__auth["entitlements_token"] = entitlements["entitlements_token"]
        except Exception:
            raise ValorantStoreException("entitlements", "request", entitlements_response)
        player_response = scraper.get("https://auth.riotgames.com/userinfo", headers=headers, timeout=15)
        try:
            player = player_response.json()
            self.__auth["player"] = player["sub"]
        except Exception:
            raise ValorantStoreException("player", "request", player_response)
        with open(self.__auth_file, "wb") as auth:
            pickle.dump(self.__auth, auth)

    def wallet(self) -> dict:
        response = self.request.get(f"https://pd.{self.__region}.a.pvp.net/store/v1/wallet/{self.__auth['player']}",
                                    headers=self.headers)
        try:
            return response.json()
        except Exception:
            raise ValorantStoreException("wallet", "request", response)

    def store(self) -> dict:
        response = self.request.get(
            f"https://pd.{self.__region}.a.pvp.net/store/v2/storefront/{self.__auth['player']}",
            headers=self.headers)
        try:
            return response.json()
        except Exception:
            raise ValorantStoreException("store", "request", response)