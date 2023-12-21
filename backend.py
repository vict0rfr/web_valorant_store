from flask import Flask, redirect, url_for, request, render_template, session
from valorantstore import ValorantStore

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        valorant_store = ValorantStore(username=user, password=pswd, region="na")
        return render_template("index.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg")
    else:
        return render_template("index.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg")
    
@app.route('/itemshop.html', methods=['POST', 'GET'])
def itemshop():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        valorant_store = ValorantStore(username=user, password=pswd, region="na")
        return render_template("itemshop.html",
                        val_credits=valorant_store.wallet(True)["valorant_points"],
                        rad_points=valorant_store.wallet(True)["radianite_points"],
                        kingdom_credits=valorant_store.wallet(True)["kingdom_credits"],
                        bundleImg=valorant_store.store(True)["bundles"]["data"][0]["image"],
                        dailyOffer0=valorant_store.store(True)["daily_offers"]["data"][0]["image"],
                        dailyOffer1=valorant_store.store(True)["daily_offers"]["data"][1]["image"],
                        dailyOffer2=valorant_store.store(True)["daily_offers"]["data"][2]["image"],
                        dailyOffer3=valorant_store.store(True)["daily_offers"]["data"][3]["image"],      
                        bundle0=valorant_store.bundle_info(valorant_store.store(True)["bundles"]["data"][0]["id"])["displayName"],
                        item0=valorant_store.skin_info(valorant_store.store(True)["daily_offers"]["data"][0]["id"])["displayName"],
                        item1=valorant_store.skin_info(valorant_store.store(True)["daily_offers"]["data"][1]["id"])["displayName"],
                        item2=valorant_store.skin_info(valorant_store.store(True)["daily_offers"]["data"][2]["id"])["displayName"],
                        item3=valorant_store.skin_info(valorant_store.store(True)["daily_offers"]["data"][3]["id"])["displayName"],
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg"
                    )
    else:
        return render_template("itemshop.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg")
        
@app.route('/nightmarket.html', methods=['POST', 'GET'])
def nightmarket():
    if request.method == 'POST':
        user = request.form['username']
        pswd = request.form['password']
        valorant_store = ValorantStore(username=user, password=pswd, region="na")
        return render_template("nightmarket.html",
                        nightmarketname0=valorant_store.skin_info(valorant_store.store(True)["night_market"]["data"][0]["id"])["displayName"],
                        nightmarketname1=valorant_store.skin_info(valorant_store.store(True)["night_market"]["data"][1]["id"])["displayName"],
                        nightmarketname2=valorant_store.skin_info(valorant_store.store(True)["night_market"]["data"][2]["id"])["displayName"],
                        nightmarketname3=valorant_store.skin_info(valorant_store.store(True)["night_market"]["data"][3]["id"])["displayName"],
                        nightmarketname4=valorant_store.skin_info(valorant_store.store(True)["night_market"]["data"][4]["id"])["displayName"],
                        nightmarketname5=valorant_store.skin_info(valorant_store.store(True)["night_market"]["data"][5]["id"])["displayName"],
                        nightmarket0=valorant_store.store(True)["night_market"]["data"][0]["image"],
                        nightmarket1=valorant_store.store(True)["night_market"]["data"][1]["image"],
                        nightmarket2=valorant_store.store(True)["night_market"]["data"][2]["image"],
                        nightmarket3=valorant_store.store(True)["night_market"]["data"][3]["image"],
                        nightmarket4=valorant_store.store(True)["night_market"]["data"][4]["image"],
                        nightmarket5=valorant_store.store(True)["night_market"]["data"][5]["image"],
                        orgPrice0=valorant_store.store(True)["night_market"]["data"][0]["original_cost"],
                        orgPrice1=valorant_store.store(True)["night_market"]["data"][1]["original_cost"],
                        orgPrice2=valorant_store.store(True)["night_market"]["data"][2]["original_cost"],
                        orgPrice3=valorant_store.store(True)["night_market"]["data"][3]["original_cost"],
                        orgPrice4=valorant_store.store(True)["night_market"]["data"][4]["original_cost"],
                        orgPrice5=valorant_store.store(True)["night_market"]["data"][5]["original_cost"],
                        discountPrice0=valorant_store.store(True)["night_market"]["data"][0]["discount_cost"],
                        discountPrice1=valorant_store.store(True)["night_market"]["data"][1]["discount_cost"],
                        discountPrice2=valorant_store.store(True)["night_market"]["data"][2]["discount_cost"],
                        discountPrice3=valorant_store.store(True)["night_market"]["data"][3]["discount_cost"],
                        discountPrice4=valorant_store.store(True)["night_market"]["data"][4]["discount_cost"],
                        discountPrice5=valorant_store.store(True)["night_market"]["data"][5]["discount_cost"],
                        logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg"
                    )
    else:
        return render_template("nightmarket.html", logo="https://www.svgrepo.com/show/424912/valorant-logo-play-2.svg")
        
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
# make log in change to logged in as: username
if __name__ == '__main__':
    app.run(debug=True)