import requests

page_default_values = {
    'btc': '1',
    'usd': '64639'
}

test_values = {
    'negative_btc': '-1',
    'negative_usd': '-64639',
    'zero': '0',
    'letters': 'asda',
    'space_bar': ' ',
    'empty': '',
    'positive_1_dec': 1.1,
    'positive_2_dec': 2.22,
    'positive_3_dec': 3.333,
    'positive_7_dec': 1.1111111,
    'positive_8_dec': 2.22222222,
    'positive_9_dec': 3.333333333
}

rates_source = requests.get('https://15430b599e434b43885aeb307fdd4276.api.mockbin.io/')
btc_usd_rate = rates_source.json()['data'][0]['btc']['usd']
