import json
from tabnanny import check

import requests
import pytest
import check_request_and_response

class TestApi:
    checker = check_request_and_response.Checker
    baseUrl: str = "https://backend-v2.portal-sekolah.com"
    school_list_path: str = "/api/v2/school/schools/"
    school_list_params = {"page_size":"9999"}
    login_path = "/api/v2/auth/login/"

    def test_get_school_list(self):
        response = requests.get(TestApi.baseUrl + TestApi.school_list_path,
                                params=TestApi.school_list_params,
                                )
        TestApi.checker.check_request(self, response)

        httpCode = response.status_code
        assert httpCode == 200, f'http response code is wrong, got {httpCode}, should be 200'
        print(f'\nSchool List: success validate http response code is {httpCode}')

        jsonBody = response.json()
        code = jsonBody['code']
        assert code == 200, f'code in response body is wrong, actual:{code}, expected:200'
        print(f'School List: success validate json response code is {code}\n')
        print("=========================================================================================================")

    def test_post_login_student(self):
        loginBody = {
            "login": "student.vpnsmp1_01",
            "school_id": 1469,
            "password": "portal732"
        }
        response = requests.post(TestApi.baseUrl + TestApi.login_path,
                                json=loginBody,
                                )
        TestApi.checker.check_request(self, response)

        httpCode = response.status_code
        assert httpCode == 201, f'http response code is wrong, got {httpCode}, should be 201'
        print(f'\nLogin: success validate http response code is {httpCode}')

        jsonBody = response.json()
        code = jsonBody['code']
        assert code == 201, f'code in response body is wrong, actual:{code}, expected:201'
        print(f'Login: success validate json response code is {code}')
        print("=========================================================================================================")
        TestApi.checker.check_response_body(self, response)