def application(environ, start_response):
    string = str(environ["QUERY_STRING"])
    body = string.replace("&", "\n")
    status = "200 OK"
    headers = [("Content-Type", "text/plan")]
    start_response(status, headers)
    print(body)
