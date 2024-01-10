import sys
import requests

def get_dxvk():
    json = requests.get('https://api.github.com/repos/doitsujin/dxvk/releases/latest').json()

    dxvk_version = json['tag_name'][1:]
    asset_name = f'dxvk-{dxvk_version}.tar.gz'
    new_asset_name = 'dxvk.tgz'
    asset = next((asset for asset in json['assets'] if asset['name'] == asset_name), None)

    if asset:
        asset_url = asset['browser_download_url']
        print(f'Downloading DXVK {dxvk_version}: {asset_name}')
        response = requests.get(asset_url)
        with open(new_asset_name, 'wb') as file:
            file.write(response.content)
        return f'Successfully downloaded DXVK {dxvk_version} as {new_asset_name}'
    else:
        return f'Unable to locate: {asset_name}'
        sys.exit(1) # failed workflow

if __name__ == "__main__":
    result = get_dxvk()
    print(result)
