from tokenize import cookie_re

import requests
import check_request_and_response
import configparser

from test_requestsApi.Api_notes import TestApi
from utilize.configurations import *
from utilize.resourcePath import ResourcePath as path
from utilize.payload import *

class TestLoginToSubmitQuizPsRefactor:

    checker = check_request_and_response.Checker
    accessToken = None
    session = requests.session()

    def test_get_school_list(self):
        url = getConfig()['PS-STAGING-V2']['baseUrl'] + path.V2SchoolList
        params = {"page_size":"9999"}

        response = self.session.get(url, params=params)

        #For Check Request Body / Header Only
        self.checker.check_request(response)
        self.checker.check_response_headers(response)

        #Validation
        httpStatusCode = response.status_code
        assert httpStatusCode == 200, f'httpStatusCode Expected is 200, but got {httpStatusCode}'
        jsonBody = response.json()
        assert jsonBody['code'] == 200, f'code in json body Expected is 200, but got:{jsonBody['code']}'
        print(f'\nSCHOOL LIST: success validate http response code is {httpStatusCode}')
        print(f'SCHOOL LIST: success validate json response code is {jsonBody['code']}')

        print("=========================================================================================================")

    def test_post_login_student(self):
        url = getConfig()['PS-STAGING-V2']['baseUrl'] + path.V2Login
        payloadLogin = loginPayLoads()
        response = self.session.post(url, json=payloadLogin)

        #For Check Request Body / Header Only
        self.checker.check_request(response)
        self.checker.check_response_headers(response)

        # Validation
        httpStatusCode = response.status_code
        assert httpStatusCode == 201, f'httpStatusCode Expected is 201, but got {httpStatusCode}'
        jsonBody = response.json()
        assert jsonBody['code'] == 201, f'code in json body Expected is 201, but got:{jsonBody['code']}'
        accessToken = jsonBody['data']['jwt']['access']
        TestLoginToSubmitQuizPsRefactor.accessToken = accessToken
        print(f'\ncetak token : {TestLoginToSubmitQuizPsRefactor.accessToken[-5:]}')
        print(f'LOGIN: success validate http response code is {httpStatusCode}')
        print(f'LOGIN: success validate json response code is {jsonBody['code']}')

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
