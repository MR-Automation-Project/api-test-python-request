import json
import requests
import pytest

class TestApi:

    baseUrl: str = "https://backend-v2.portal-sekolah.com"
    school_list_path: str = "/api/v2/school/schools/"
    school_list_params = {"page_size":"9999"}

    def test_get_school_list(self):
        response = requests.get(TestApi.baseUrl + TestApi.school_list_path,
                                params=TestApi.school_list_params,
                                )

        print("\n\n--------------------------------------------------- REQUEST HEADER & BODY --------------------------------------------------------")
        print(f'\nRequest Method: {response.request.method}')
        print(f'Request URL: {response.request.url}')
        print(f'Request Header: {response.request.headers}')
        print(f'Request Body: {response.request.body}')


        print("\n--------------------------------------------------- RESPONSE HTTP & HEADER --------------------------------------------------------------------")
        print(f'Response code : {response.status_code}')
        print(f'Response Headers : {response.headers}')
        print(f'Response Cookies : {response.cookies}')
        print(f'Response URL : {response.url}')
        print(f'Response is_redirect? : {response.is_redirect} - {response.is_permanent_redirect}')


        print("\n---------------------------------------------------RESPONSE BODY--------------------------------------------------------")
        print(f'ini response dalam bentuk json yang otomatis diconvert ke python structure DICT / LIST:\n {response.json()}')
        print(f'\nini response dalam bentuk text mentah sesuai balikan response dari server \n {response.text}')


        print("\n\n---------------------------------------------------VALIDATION / CHECK DATA--------------------------------------------------------")
        responseBodyJson = response.json()
        print(f'data count adalah {responseBodyJson["count"]}')

        ## jika spt ini akan error, karena blm diconvert dengan json format, tidak dapat diolah/diparsing spt contoh diatas!
        # responseBodyText = response.text
        # print(responseBodyText["count"])