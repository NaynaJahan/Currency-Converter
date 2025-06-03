import requests

def get_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.status_code, response.text
        else:
            return response.status_code, f"Error: {response.status_code} - {response.reason}"
    except Exception as e:
        return 500, str(e)