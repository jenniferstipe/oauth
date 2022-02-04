import sys
import requests
import json
import logging
import time

logging.captureWarnings(True)

test_api_url = "https://apigw-pod1.dm-us.informaticacloud.com/t/apim.usw1.com/get_employee_details"

##
##    function to obtain a new OAuth 2.0 token from the authentication server
##
def get_new_token():

	auth_server_url = "https://dm-us.informaticacloud.com/authz-service/oauth/token"
	client_id = 'Jl88QzqE3GYvaibOVb1Fx'
	client_secret = '9xy23jdl'

	token_req_payload = {'grant_type': 'client_credentials'}

	token_response = requests.post(auth_server_url,
	data=token_req_payload, verify=False, allow_redirects=False,
	auth=(client_id, client_secret))

	print(token_response)			 
	if token_response.status_code !=200:
		print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
		sys.exit(1)
	print("Successfuly obtained a new token")
	tokens = json.loads(token_response.text)
	return tokens['access_token']

## 
## 	obtain a token before calling the API for the first time
## 	the token is valid for 15 minutes
##
	token = get_new_token()

	while True:

##
##   call the API with the token
##
		api_call_headers = {'Authorization': 'Bearer ' + token}
		api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

##
##
		if	api_call_response.status_code == 401:
			token = get_new_token()
		else:
			print(api_call_response.text)

		time.sleep(30)

def main():
	get_new_token()

if __name__ == "__main__":
    main()