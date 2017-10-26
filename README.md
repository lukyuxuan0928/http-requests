# Requests

A very simple of http services library for python

## Getting Started

Here I'm using the tornado web api service to implement that how we use the simple requests to create a request and send it to the specified server.

## Installation

In order to use the requests, you need to install:

```
    1. $ sudo apt-get install python-requests
```

## Example

First, you need to initial the server ip address as a url, and pass the params what you want.

```
    ip_addr = "localhost"   # ip address
    port = 5124             # port
    url = 'http://%s:%d/api/do' %(ip_addr, port)
    params = {
        'type': 'direct_ping'
    }

```

Create a request

```
    r = requests.get(url, params=params)
```

We can check the url with parameter wherther correct or not

```
    print r.url
```

We can simply get the response from server

```
    print r.text
```

## Version

Please take note that might minor changes of syntax on different version

```
    python          == 2.7.12
    python-requests == 2.9.1
    python-tornado  == 4.2.1
    gunicorn        == 19.7.1
```