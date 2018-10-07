from flask import Flask, request
app = Flask(__name__)

import requests
import json
#currency dictionary
currency_dict={}

#ETH-USD
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=ETH')
r_eth = r.json()
# print("1 ETH in USD is " +str(r_eth['data']['1027']['quotes']['USD']['price']))
currency_dict["USD"]=1/r_eth['data']['1027']['quotes']['USD']['price']
#ETH-EUR
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=EUR')
r_eth = r.json()
# print("1 ETH in EUR is " +str(r_eth['data']['1027']['quotes']['EUR']['price']))
currency_dict["EUR"]=1/r_eth['data']['1027']['quotes']['EUR']['price']
#ETH-JPY
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=JPY')
r_eth = r.json()
# print("1 ETH in JPY is " +str(r_eth['data']['1027']['quotes']['JPY']['price']))
currency_dict["JPY"]=1/r_eth['data']['1027']['quotes']['JPY']['price']
#ETH-INR
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=INR')
r_eth = r.json()
# print("1 ETH in INR is " +str(r_eth['data']['1027']['quotes']['INR']['price']))
currency_dict["INR"]=1/r_eth['data']['1027']['quotes']['INR']['price']
#ETH-CNY
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=CNY')
r_eth = r.json()
# print("1 ETH in CNY is " +str(r_eth['data']['1027']['quotes']['CNY']['price']))
currency_dict["CNY"]=1/r_eth['data']['1027']['quotes']['CNY']['price']
#ETH-BTC
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=BTC')
r_eth = r.json()
# print("1 ETH in BTC is " +str(r_eth['data']['1027']['quotes']['BTC']['price']))
currency_dict["BTC"]=r_eth['data']['1027']['quotes']['BTC']['price']
#ETH-XRP
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=XRP')
r_eth = r.json()
# print("1 ETH in XRP is " +str(r_eth['data']['1027']['quotes']['XRP']['price']))
currency_dict["XRP"]=r_eth['data']['1027']['quotes']['XRP']['price']
#ETH-LTC
r = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=LTC')
r_eth = r.json()
# print("1 ETH in LTC is " +str(r_eth['data']['1027']['quotes']['LTC']['price']))
currency_dict["LTC"]=r_eth['data']['1027']['quotes']['LTC']['price']


for k,v in currency_dict.items():
            print(k, v)

adjust = 1000000000

@app.route("/convert")
def hello():
    curr = request.args.get('curr')
    val = request.args.get('val')

    if curr != None:
        # assuming value is 1
        if val == None or val == "":
            val = 1
        else:
            val = int(val)

        ret_ = {}

        ret_['value'] = int(adjust * val * currency_dict[curr])

        return json.dumps(ret_)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


