import httplib2
import webbrowser
from pprint import pprint

http = httplib2.Http()
bin_url = 'https://httpbin.org/'

post_data = '{"name": "Chisom", "city": "Harrison"}'

resp,data = http.request('https://httpbin.org/post', method = 'POST', body = post_data, headers = {'content-type':'application/json'})
pprint(resp)
