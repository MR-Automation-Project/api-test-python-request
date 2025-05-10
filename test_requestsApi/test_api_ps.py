import json

import requests
import check_request_and_response
from utilize.configurations import *
from utilize.resourcePath import ResourcePath as path
from utilize.payload import Payload

class TestLoginToSubmitQuizPsRefactor:

    checker = check_request_and_response.Checker
    accessToken = None
    session = requests.session()
    baseUrl = getConfig()['ENV-STAGING-V2']['baseUrl']

    def test_search_school_list(self):
        path_search_school = path.V2SchoolList
        params = {"page_size":"20", "search":"Smp V"}

        response = self.session.get(self.baseUrl, params=params)

        #Validation
        httpStatusCode = response.status_code
        assert httpStatusCode == 200, f'httpStatusCode Expected is 200, but got {httpStatusCode}'
        jsonBody = response.json()
        assert jsonBody['code'] == 200, f'code in json body Expected is 200, but got:{jsonBody['code']}'
        print(f'\nSCHOOL LIST: success validate http response code is {httpStatusCode}')
        print(f'SCHOOL LIST: success validate json response code is {jsonBody['code']}')

        print("=========================================================================================================")

    def test_login_with_valid_users_and_password(self):
        endpoint = getConfig()['ENV-STAGING-V2']['baseUrl'] + path.V2Login
        params = None

        login = self.session.post(endpoint, params=params, json=Payload.payload_login_student())

        #asset status code
        assert login.status_code == 201, f"Expected status code 201 but got {login.status_code}"

        #assert JSON body before Parsing
        try:
            jsonBody = login.json()
            print(jsonBody)  # Print the whole body for review

        except json.JSONDecodeError:
            assert False, f"Response body is not valid JSON. Received: {login.text}"
            # return  # Exit if body is not JSON

        # Check if top-level keys are exist
        assert "error" in jsonBody, "Response body is missing 'error' key"
        assert "code" in jsonBody, "Response body is missing 'code' key"
        assert "message" in jsonBody, "Response body is missing 'message' key"
        assert "data" in jsonBody, "Response body is missing 'data' key"

        # Validate top-level values for success (status 201)
        assert jsonBody["error"] is False, f"Expected 'error' value to be False but got {jsonBody['error']}"
        assert jsonBody["code"] == 201, f"Expected 'code' value is 201 but got {jsonBody['code']}"

        # Validate 'data' field (Assuming 'data' is a dictionary)
        assert isinstance(jsonBody["data"], dict), f"Expected 'data' to be a dictionary but got {type(jsonBody['data'])}"

        #Validate some critical keys are exist in the 'data' object
        data = jsonBody["data"]
        data_Jwt = jsonBody["data"]["jwt"]
        assert "access" in data_Jwt, "Missing 'access' in data"
        assert "refresh" in data_Jwt, "Missing 'refresh' in data"
        assert "id" in data, "Missing 'id' in data"
        assert "username" in data, "Missing 'username' in data"
        assert "name" in data, "Missing 'name' in data"
        assert "status" in data, "Missing 'status' in data"
        assert "school_id" in data, "Missing 'school_id' in data"
        assert "school_name" in data, "Missing 'school_names' in data"

        # Validate types (adjust types as per your API response)
        assert isinstance(data_Jwt["access"], str), f"Expected 'access' to be a string, but got {data_Jwt["access"]}"
        assert isinstance(data_Jwt["refresh"], str), f"Expected 'refresh' to be a string, but got {data_Jwt["refresh"]}"
        assert isinstance(data["school_id"], int), f"Expected 'school_id' to be an integer, but got {data["school_id"]}"
        assert isinstance(data["status"], str), f"Expected 'status' to be an string, but got {data["status"]}"

        # Validate some values of critical fields (adjust as needed)
        assert data_Jwt["access"], "Access token should not be empty"  # Check if not empty string
        assert data_Jwt["refresh"], "Refresh token should not be empty"
        assert data["picture"] is None, "picture should be null"  # Check if null / None

        ##Storing access token to variable
        print("\nCool..!!, Login successful and all validation is passed!")
        access_token = jsonBody['data']['jwt']['access']
        TestLoginToSubmitQuizPsRefactor.accessToken = access_token

        print("\n---------REQUEST HEADERS-----------------")
        for req_headers_name, req_headers_value in login.request.headers.items():
            print(f"\n{req_headers_name}: {req_headers_value}")
        print("\n---------RESPONSE HEADERS----------------------------")
        for res_headers_name, res_headers_value in login.headers.items():
            print(f"\n{res_headers_name}: {res_headers_value}")





        # #For Check Request Body / Header Only
        # self.checker.check_request(response)
        # self.checker.check_response_headers(response)
        #
        # # Validation
        # httpStatusCode = response.status_code
        # assert httpStatusCode == 201, f'httpStatusCode Expected is 201, but got {httpStatusCode}'
        # jsonBody = response.json()
        # assert jsonBody['code'] == 201, f'code in json body Expected is 201, but got:{jsonBody['code']}'

        # print(f'\ncetak token : {TestLoginToSubmitQuizPsRefactor.accessToken[-5:]}')
        # print(f'LOGIN: success validate http response code is {httpStatusCode}')
        # print(f'LOGIN: success validate json response code is {jsonBody['code']}')

        print("=========================================================================================================")

    #
    # # def get_token(test_login_student):
    # #     accessToken = jsonBody["data"]["jwt"]["access"]
    # #     assert accessToken is not None, f'accessToken gagal ter-extract'
    # #     return accessToken
    # #
    # # def test_loggedinusersdetailsnew(self):
    # #     acctoken = self.test_login_student().get_token()
    # #     headers = {"Authorization": f"Bearer {acctoken}"}
    # #     response = requests.get(TestApi.baseUrl + TestApi.loggedinusersdetails_path,
    # #                              headers=headers
    # #                              )
    # #
    # #     # Validate http status_code
    # #     httpCodeLoggedinUsersDetails = response.status_code
    # #     assert httpCodeLoggedinUsersDetails == 200, f'http response code is wrong, got {httpCodeLoggedinUsersDetails}, should be 200'
    # #     print(f'\nLoggedInUsersDetailsNew: success validate http response code is {httpCodeLoggedinUsersDetails}')
    # #     # if httpCode == 500:
    # #     #     jsonBody = response.json()
    # #     #     print(f'got error 500 with message is {jsonBody["message"]}')
