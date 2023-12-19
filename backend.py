from flask import Flask, redirect, url_for, request, render_template
from valorantstore import ValorantStore

valorant_store = ValorantStore(username="jjerf", password="jaimeslespenis69", region="na")

app = Flask(__name__)

@app.route('/')
def parseStore():
    return render_template("index.html",
                        val_credits=valorant_store.wallet(True)["valorant_points"],
                        rad_points=valorant_store.wallet(True)["radianite_points"],
                        kingdom_credits=valorant_store.wallet(True)["kingdom_credits"],
                        bundle0=valorant_store.store(True)["bundles"]["data"][0]["image"],
                        dailyOffer0=valorant_store.store(True)["daily_offers"]["data"][0]["image"],
                        dailyOffer1=valorant_store.store(True)["daily_offers"]["data"][1]["image"],
                        dailyOffer2=valorant_store.store(True)["daily_offers"]["data"][2]["image"],
                        dailyOffer3=valorant_store.store(True)["daily_offers"]["data"][3]["image"],      
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg",
                    )

if __name__ == '__main__':
    app.run(debug=True)