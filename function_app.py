import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.function_name(name="txdev1")
@app.route(route="/{fn}/{a?}/{b?}", auth_level=func.AuthLevel.ANONYMOUS)
def txdev(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('url ' + req.url)
    
    rsp = "{}"

    if "/metadata?mode=terminology" in req.url:
        rsp = readfile("terminology.json")
    elif "/metadata" in req.url:
        rsp = readfile("metadata.json")
    else:
        rsp = readfile("tx-reg-hl7.json")
    # elif "jurisdiction" in req.url or "urn:iso:std:iso:3166" in req.url:
    #     rsp = readfile("tx-reg-hl7.json")
    # elif "languages" in req.url or "common-languages-australia" in req.url or "unitsofmeasure.org" in req.url or "units-of-time" in req.url or "www.rcpa.edu.au" in req.url or "www.iana.org" in req.url or "au-timezone" in req.url or "urn:ietf:bcp:47" in req.url:
    #     rsp = readfile("tx-reg.json")
    # else:
    #     rsp = readfile("tx-reg-csiro.json")
        
    logging.info(rsp)
        
    return func.HttpResponse(
      rsp,
      headers = {'Content-Type' : 'application/json'},
      status_code=200
    )
    

def readfile(path):
    with open(path, 'rb') as f:
        return f.read()

