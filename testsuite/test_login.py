from shared.page_objects.login_page import LoginPage
from shared.api_client.api_service import ApiService
from shared.utils.logger import log, fail
from unittest.mock import patch

# Initialize page objects and API service
login_page = LoginPage()
api_service = ApiService()

# Function to test both UI and API login
@patch('requests.post')
def test_login(mock_post):
    # Mock API response
    mock_response = {'token': 'mock-token-12345'}
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    # Step 1: Perform UI login
    log("Starting UI login...")
    try:
        login_page.login("testuser", "password123")
        log("UI login successful.")
    except Exception as e:
        fail(f"UI login failed: {str(e)}")

    # Step 2: Perform API login
    log("Starting API login...")
    try:
        token = api_service.login("testuser", "password123")
        log(f"API login successful. Token: {token}")
    except Exception as e:
        fail(f"API login failed: {str(e)}")

# Execute the test
test_login()