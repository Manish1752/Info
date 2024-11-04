import requests

cookies = {
    'source': 'mb',
    '_gid': 'GA1.2.1236421304.1706295770',
    '_gat_gtag_UA_137597827_4': '1',
    'session_key': 'hnl4y8xtfe918iiz2go67z85nsrvwqdn',
    '_ga': 'GA1.2.1006342705.1706295770',
    'datadome': '3AmY3lp~TL1WEuDKCnlwro_WZ1C6J66V1Y0TJ4ITf1Hvo4833Fh4LF3gHrPCKFJDPUPoXh2dXQHJ_uw0ifD8jmCaDltzE5T3zzRDbXOKH9rPNrTFs29DykfP3cfo7QGy',
    '_ga_R04L19G92K': 'GS1.1.1706295769.1.1.1706295794.0.0.0',
}

headers = {
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://shop.garena.sg',
    'Referer': 'https://shop.garena.sg/app/100067/idlogin',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-datadome-clientid': 'DLm2W1ajJwdv~F~a_1d_1PyWnW6ns7GY5ChVcZY3HJ9r6D29661473aQaL2~3Nfh~Vf3m7rie7ObIb1_3eRN7J0G6uFZhMq5pM2jA828fE1dS7rZ7H3MWGQ5vGraAQWd',
}

def get_data(uid):
    json_data = {
        'app_id': 100067,
        'login_id': uid,
        'app_server_id': 0,
    }
    
    try:
        response = requests.post('https://shop.garena.sg/api/auth/player_id_login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

uid = input("Enter Your Uid: ")
data = get_data(uid)
if data:
    # If you need to decode escaped characters
    decoded_text = data.encode('utf-8').decode('unicode-escape')
    print(decoded_text)
else:
    print("No data received.")
