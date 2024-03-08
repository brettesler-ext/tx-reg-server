import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="txdev", auth_level=func.AuthLevel.FUNCTION)
def txdev(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('txdev')
    
    rsp = readfile("metadata.json")

    if "/metadata?mode=terminology" in req.url:
        rsp = "{}"

    return func.HttpResponse(
      rsp,
      headers = {'Content-Type' : 'application/json'},
      status_code=200
    )

def readfile(path):
    with open(path, 'rb') as f:
        return f.read()

