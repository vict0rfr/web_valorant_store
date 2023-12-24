from flask import Flask, redirect, url_for, request, render_template, session
from valorantstore import ValorantStore
import requests
from humanfriendly import format_timespan
from datetime import timedelta
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=5)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='None',
)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        session['user'] = user
        session['pswd'] = pswd
        session.permanent = True
        return render_template("index.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg", login="Logged in as: " + user,)
    else:
        if "user" in session and "pswd" in session:
            user = session["user"]
            pswd = session["pswd"]
            return render_template("index.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg", login="Logged in as: " + user,)
        else:
            return render_template("index.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg", login="Login")

@app.route('/itemshop.html', methods=['POST', 'GET'])
def itemshop():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        session.permanent = True
        session['user'] = user
        session['pswd'] = pswd
        valorant_store = ValorantStore(username=user, password=pswd, region="na")
        store = valorant_store.store(False)
        wallet = valorant_store.wallet(False)
        return render_template("itemshop.html",
                        val_credits=wallet["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                        rad_points=wallet["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"],
                        kingdom_credits=wallet["Balances"]["85ca954a-41f2-ce94-9b45-8ca3dd39a00d"],
                        bundleImg=f"https://media.valorant-api.com/bundles/{store['FeaturedBundle']['Bundles'][0]['DataAssetID']}/displayicon.png",
                        bundle0=(requests.get(f"https://valorant-api.com/v1/bundles/{store['FeaturedBundle']['Bundles'][0]['DataAssetID']}").json())["data"]["displayName"],
                        bundlePrice0=str(store["FeaturedBundle"]["Bundles"][0]["TotalDiscountedCost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        dailyOffer0=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][0]['OfferID']}/displayicon.png",
                        dailyOffer1=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][1]['OfferID']}/displayicon.png",
                        dailyOffer2=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][2]['OfferID']}/displayicon.png",
                        dailyOffer3=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][3]['OfferID']}/displayicon.png",      
                        item0=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][0]['OfferID']}").json()["data"]["displayName"],
                        item1=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][1]['OfferID']}").json()["data"]["displayName"],
                        item2=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][2]['OfferID']}").json()["data"]["displayName"],
                        item3=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][3]['OfferID']}").json()["data"]["displayName"],
                        price0=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][0]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        price1=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][1]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        price2=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][2]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        price3=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][3]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        timeleft_shop="Time left: " + format_timespan(store["SkinsPanelLayout"]["SingleItemOffersRemainingDurationInSeconds"]),
                        login="Logged in as: " + user, 
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg"
                    )
    else:
        if "user" in session and "pswd" in session:
            user = session["user"]
            pswd = session["pswd"]
            session.permanent = True
            valorant_store = ValorantStore(username=user, password=pswd, region="na")
            store = valorant_store.store(False)
            wallet = valorant_store.wallet(False)
            return render_template("itemshop.html",
                        val_credits=wallet["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                        rad_points=wallet["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"],
                        kingdom_credits=wallet["Balances"]["85ca954a-41f2-ce94-9b45-8ca3dd39a00d"],
                        bundleImg=f"https://media.valorant-api.com/bundles/{store['FeaturedBundle']['Bundles'][0]['DataAssetID']}/displayicon.png",
                        bundle0=(requests.get(f"https://valorant-api.com/v1/bundles/{store['FeaturedBundle']['Bundles'][0]['DataAssetID']}").json())["data"]["displayName"],
                        bundlePrice0=str(store["FeaturedBundle"]["Bundles"][0]["TotalDiscountedCost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        dailyOffer0=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][0]['OfferID']}/displayicon.png",
                        dailyOffer1=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][1]['OfferID']}/displayicon.png",
                        dailyOffer2=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][2]['OfferID']}/displayicon.png",
                        dailyOffer3=f"https://media.valorant-api.com/weaponskinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][3]['OfferID']}/displayicon.png",      
                        item0=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][0]['OfferID']}").json()["data"]["displayName"],
                        item1=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][1]['OfferID']}").json()["data"]["displayName"],
                        item2=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][2]['OfferID']}").json()["data"]["displayName"],
                        item3=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['SkinsPanelLayout']['SingleItemStoreOffers'][3]['OfferID']}").json()["data"]["displayName"],
                        price0=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][0]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        price1=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][1]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        price2=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][2]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        price3=str(store["SkinsPanelLayout"]["SingleItemStoreOffers"][3]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        timeleft_shop="Time left: " + format_timespan(store["SkinsPanelLayout"]["SingleItemOffersRemainingDurationInSeconds"]),
                        login="Logged in as: " + user, 
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg"
                    )
        else:
            return render_template("itemshop.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg", login="Login")
        
@app.route('/nightmarket.html', methods=['POST', 'GET'])
def nightmarket():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        session.permanent = True
        session['user'] = user
        session['pswd'] = pswd
        valorant_store = ValorantStore(username=user, password=pswd, region="na")
        store = valorant_store.store(False)
        return render_template("nightmarket.html",
                        nightmarketname0=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][0]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname1=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][1]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname2=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][2]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname3=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][3]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname4=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][4]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname5=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][5]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarket0=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][0]['Offer']['OfferID']}/displayicon.png",
                        nightmarket1=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][1]['Offer']['OfferID']}/displayicon.png",
                        nightmarket2=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][2]['Offer']['OfferID']}/displayicon.png",
                        nightmarket3=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][3]['Offer']['OfferID']}/displayicon.png",
                        nightmarket4=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][4]['Offer']['OfferID']}/displayicon.png",
                        nightmarket5=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][5]['Offer']['OfferID']}/displayicon.png",
                        orgPrice0=str(store['BonusStore']['BonusStoreOffers'][0]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice1=str(store['BonusStore']['BonusStoreOffers'][1]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice2=str(store['BonusStore']['BonusStoreOffers'][2]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice3=str(store['BonusStore']['BonusStoreOffers'][3]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice4=str(store['BonusStore']['BonusStoreOffers'][4]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice5=str(store['BonusStore']['BonusStoreOffers'][5]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice0=str(store['BonusStore']['BonusStoreOffers'][0]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice1=str(store['BonusStore']['BonusStoreOffers'][1]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice2=str(store['BonusStore']['BonusStoreOffers'][2]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice3=str(store['BonusStore']['BonusStoreOffers'][3]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice4=str(store['BonusStore']['BonusStoreOffers'][4]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice5=str(store['BonusStore']['BonusStoreOffers'][5]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        timeleft_nightmarket="Time left: " + format_timespan(store["BonusStore"]["BonusStoreRemainingDurationInSeconds"]),
                        login="Logged in as: " + user,
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg"
                    )
    else:
        if "user" in session and "pswd" in session:
            user = session["user"]
            pswd = session["pswd"]
            session.permanent = True
            valorant_store = ValorantStore(username=user, password=pswd, region="na")
            store = valorant_store.store(False)
            return render_template("nightmarket.html",
                        nightmarketname0=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][0]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname1=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][1]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname2=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][2]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname3=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][3]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname4=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][4]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarketname5=requests.get(f"https://valorant-api.com/v1/weapons/skinlevels/{store['BonusStore']['BonusStoreOffers'][5]['Offer']['OfferID']}").json()["data"]["displayName"],
                        nightmarket0=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][0]['Offer']['OfferID']}/displayicon.png",
                        nightmarket1=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][1]['Offer']['OfferID']}/displayicon.png",
                        nightmarket2=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][2]['Offer']['OfferID']}/displayicon.png",
                        nightmarket3=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][3]['Offer']['OfferID']}/displayicon.png",
                        nightmarket4=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][4]['Offer']['OfferID']}/displayicon.png",
                        nightmarket5=f"https://media.valorant-api.com/weaponskinlevels/{store['BonusStore']['BonusStoreOffers'][5]['Offer']['OfferID']}/displayicon.png",
                        orgPrice0=str(store['BonusStore']['BonusStoreOffers'][0]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice1=str(store['BonusStore']['BonusStoreOffers'][1]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice2=str(store['BonusStore']['BonusStoreOffers'][2]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice3=str(store['BonusStore']['BonusStoreOffers'][3]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice4=str(store['BonusStore']['BonusStoreOffers'][4]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        orgPrice5=str(store['BonusStore']['BonusStoreOffers'][5]['Offer']["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice0=str(store['BonusStore']['BonusStoreOffers'][0]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice1=str(store['BonusStore']['BonusStoreOffers'][1]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice2=str(store['BonusStore']['BonusStoreOffers'][2]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice3=str(store['BonusStore']['BonusStoreOffers'][3]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice4=str(store['BonusStore']['BonusStoreOffers'][4]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        discountPrice5=str(store['BonusStore']['BonusStoreOffers'][5]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]) + " VBUCKS",
                        timeleft_nightmarket="Time left: " + format_timespan(store["BonusStore"]["BonusStoreRemainingDurationInSeconds"]),
                        login="Logged in as: " + user,
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg"
                    )
        return render_template("nightmarket.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg", login="Login",)
        
@app.route('/accessories.html', methods=['POST', 'GET'])
def accessories():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        valorant_store = ValorantStore(username=user, password=pswd, region="na")
        return render_template("accessories.html",

                    )
    else:
        return render_template("accessories.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg")
if __name__ == '__main__':
    app.run(debug=True)