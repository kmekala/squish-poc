import requests

class ApiService:
    API_BASE_URL = "https://api.mock.com"
    LOGIN_ENDPOINT = "/login"

    def login(self, username, password):
        url = f"{self.API_BASE_URL}{self.LOGIN_ENDPOINT}"
        payload = {"username": username, "password": password}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200 and response.json().get("token"):
                return response.json()['token']
            else:
                raise Exception(f"API Login failed: {response.status_code}")
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")