import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="txdev/{a}/{b}", auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="txdev/{a}", auth_level=func.AuthLevel.ANONYMOUS)
def txdev(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('url ' + req.url)
    
    rsp = "{}"

    if "/metadata?mode=terminology" in req.url:
        rsp = readfile("terminology.json")
    elif "/metadata" in req.url:
        rsp = readfile("metadata.json")
    elif "common-languages-australia-1" in req.url or "unitsofmeasure.org" in req.url:
        rsp = readfile("tx-reg.json")
    else:
        rsp = readfile("tx-reg-csiro.json")
        
    logging.info(rsp)
        
    return func.HttpResponse(
      rsp,
      headers = {'Content-Type' : 'application/json'},
      status_code=200
    )
    

def readfile(path):
    with open(path, 'rb') as f:
        return f.read()

