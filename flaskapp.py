from flask import Flask, request
from pathlib import Path
import os.path, json

app = Flask(__name__)

@app.route("/")
def landing():
    return "Flex."
    
def build_prices():
    price_dict = {}
    with open('prices.txt', 'r') as json_prices_file:
        for line in json_prices_file:
            [item,price] = line.split('\t')
            price_dict[item] = price.rstrip()
            
    json_file = open("prices.json","w+")
    json_file.write(json.dumps(price_dict, sort_keys=True,
        indent=4, separators=(',', ': ')))
    json_file.close()
        

@app.route('/prices', methods=['GET', 'POST'])
def prices():
    json_prices = Path("prices.json")
    if not json_prices.is_file():
        build_prices()
        
    with open('prices.json', 'r') as json_prices_file:
        json_content = json_prices_file.read()
        return json_content
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')