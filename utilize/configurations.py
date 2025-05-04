import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('D:\\ORG_REPO\\MR-Automation-Project\\api-test-python-request\\utilize\\properties.ini')
    return config

def storeAccessToken(access_token):
    global accessToken
    accessToken = access_token
    return accessToken
print(storeAccessToken)


