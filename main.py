import requests
import tornado.web

if __name__ == "__main__":
    # Initial variable
    ip_addr = "localhost"   # ip address
    port = 5124             # port
    url = 'http://%s:%d/api/do' %(ip_addr, port)
    params = {
        'type': 'direct_ping'
    }

    # Create a request
    r = requests.get(url, params=params)

    # Check the url
    print r.url

    # Print the response from server
    print r.text













