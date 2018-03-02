from mitmproxy import http

def response(flow: http.HTTPFlow):
    if "set-cookie" in flow.response.headers:
        print(flow.response.headers["set-cookie"])
