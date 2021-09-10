from time import sleep
import requests


def call_request(method, endpoint=''):
    token = 'b0fda4d894ae2e4b05a3600c1edf0568193fbb65289ca7a1e66a8a73f214b3c382ba0dcfbe6a72d981f27540de62ebc2f637691094f5bae2'
    headers = {
        "ContentType": "application/json",
        "Authorization": "Bearer " + token
    }
    method = getattr(requests, method.lower())
    res = method('http://supervisor' + endpoint, headers=headers)
    if res.status_code == 200:
        return res.json()

    return {}


if __name__ == "__main__":
    identify_key = 'ac1c0015-5227-457d-9938-82e7bf39d185'
    # Reload
    while True:
        sleep(5)
        call_request('post', '/store/reload')
        addons = call_request('get', '/addons').get('data', {}).get('addons', [])
        for addon in addons:
            if addon.get('description') == identify_key:
                if addon.get('installed') and addon.get('update_available'):
                    # Updated
                    update_res = call_request('post', '/store/addons/' + addon.get('slug') + '/update')
                    if update_res.get('result').lower() == 'ok':
                        # Rebuild
                        call_request('post', '/addons/' + addon.get('slug') + '/rebuild')
                        # Restart
                        call_request('post', '/addons/' + addon.get('slug') + '/restart')
