import requests

API_URL = "https://api.api-ninjas.com/v1/quotes"

def generate_quote(api_key):
    headers = {"X-Api-Key": api_key}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == requests.codes.ok:
        quote_obj = response.json()[0]
        return f"{quote_obj['quote']} -- {quote_obj['author']}"
    # Fall back to a default quote if the API fails
    return "Just do it! -- Shia LaBeouf"
