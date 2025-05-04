import json
import requests

class Checker:
    def check_request(response: requests.Response):
        print(f'\nRequest Method: {response.request.method}')
        print(f'Request URL: {response.request.url}')
        print(f'Request Header: {response.request.headers}')
        print(f'Request Body: {response.request.body}')
        #
        #
    def check_response_headers(response: requests.Response):
        # print("\n--------------------------------------------------- RESPONSE HTTP & HEADER --------------------------------------------------------------------")
        print(f'Response code : {response.status_code}')
        print(f'Response Headers : {response.headers}')
        print(f'Response Cookies : {response.cookies}')
        print(f'Response URL : {response.url}')
        print(f'Response is_redirect? : {response.is_redirect} - {response.is_permanent_redirect}')
        print(f'Response time : {response.elapsed}')
        #
        #
        # print("\n---------------------------------------------------RESPONSE BODY--------------------------------------------------------")
    def check_response_body(response: requests.Response):
        print(f'ini response dalam bentuk json yang otomatis diconvert ke python structure DICT / LIST:\n {response.json()}')
        print(f'\nini response dalam bentuk text mentah sesuai balikan response dari server \n {response.text}')
        print(f'body message: {response.json()["message"]}')
        print(f'body code: {response.json()["code"]}')