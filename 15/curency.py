import json
import pprint
import urllib.request
import webbrowser
#webbrowser.open('http://data.fixer.io/api/latest?access_key=df36769ca30746523ddcb41f1e0e7faa')
response = urllib.request.urlopen('http://data.fixer.io/api/latest?access_key=df36769ca30746523ddcb41f1e0e7faa')
data = response.read()


python_data = json.loads(data)
#pprint.pprint(python_data)
def convert_currency(amount, from_currency, to_currency):
    return print(amount*python_data['rates'][to_currency]/python_data['rates'][from_currency])
convert_currency(100,"BGN","EUR")