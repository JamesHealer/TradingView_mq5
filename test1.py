import requests
import numpy as np

def get_account():
    try:
        headers = {
            "Cookie": 'cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={"analytics":true,"advertising":true}; _ga=GA1.1.1767084649.1711335304; device_t=VGVXT0JBOjA.MXpjQum_00hiufTbe3K3Y-I-P43M1KxZvl8_NcFiJtk; _gcl_au=1.1.1232345717.1711411945; theme=light; sessionid=6zm0thsw5qzadcdgy1c333o260effidr; sessionid_sign=v2:VaHQE3nWv9adYk6Am31e/c4kyH0G62/0CKaOVcxhBE4=; etg=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; cachec=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; png=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; tv_ecuid=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; _ga_53M0R0ZT9V=GS1.1.1711733524.4.0.1711733524.0.0.0; _ga_R53B6WMR8T=GS1.1.1711733524.4.1.1711733525.0.0.0; _ga_YVVRYGL0E0=GS1.1.1711731448.41.1.1711736640.36.0.0; _sp_id.cf1a=b9fd07d7-91d8-405d-98ea-45006c6e0cdb.1711335298.23.1711736642.1711734659.c97edd33-356d-4e91-a691-2c8f92a180ae; _sp_ses.cf1a=*',
            "Origin": 'https://www.tradingview.com',
            "Referer": 'https://www.tradingview.com'
        }

        payload = {
            "username": "jameshealer715",
            "password": "Healer715!@#",
            "locale": "en"
        }

        response = requests.post(
            'https://papertrading.tradingview.com/trading/accounts',
            json=payload,
            headers=headers
        )

        response.raise_for_status()

        account_data = response.json()
        account_id = account_data[0].get('accountId')
        return account_id

    except requests.exceptions.RequestException as e:
        print('Error retrieving account:', e)

account_id = get_account()

def get_orders():
    try:
        headers = {
            "Cookie": 'cookiePrivacyPreferenceBannerProduction=notApplicable; cookiesSettings={"analytics":true,"advertising":true}; _ga=GA1.1.1767084649.1711335304; device_t=VGVXT0JBOjA.MXpjQum_00hiufTbe3K3Y-I-P43M1KxZvl8_NcFiJtk; _gcl_au=1.1.1232345717.1711411945; theme=light; _ga_R53B6WMR8T=GS1.1.1711793128.5.0.1711793128.0.0.0; _ga_53M0R0ZT9V=GS1.1.1711793128.5.0.1711793128.0.0.0; _sp_ses.cf1a=*; sessionid=twk5lyawsdd8gbbl32fw6s5n0xv1kwaf; sessionid_sign=v2:FplWSJBgvc+tIzttwKZBWpIO6/toP1WvCvtp1rUFWHc=; png=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; etg=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; cachec=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; tv_ecuid=9d3bdda4-64b0-4a01-88bd-6ad44910b35a; _sp_id.cf1a=b9fd07d7-91d8-405d-98ea-45006c6e0cdb.1711335298.34.1711846197.1711841822.acb2bf90-daf1-441f-97dd-f269fd2c1e18; _ga_YVVRYGL0E0=GS1.1.1711841445.53.1.1711846214.7.0.0',
            "Origin": 'https://www.tradingview.com',
            "Referer": 'https://www.tradingview.com',
            "Content-Type": "application/json"  # Specify the content type of the request
        }

        payload = {
            "param": account_id,
        }

        response = requests.post(
            'https://papertrading.tradingview.com/trading/account/',
            json=payload,
            headers=headers
        )

        response.raise_for_status()

        order_data = response.json()
        positions = order_data.get('positions')
        return positions

    except requests.exceptions.RequestException as e:
        print('Error retrieving orders:', e)

def send_orders_to_server(orders):
    server_url = 'http://localhost:5000'
    response = requests.post(server_url + '/orders', json=orders)
    if response.status_code == 200:
        print('Orders sent to server successfully.')
    else:
        print('Failed to send orders to server.')

orders = get_orders()
print("Order data:", orders)
print("Order count is:", len(orders))

# Example usage
send_orders_to_server(orders)
