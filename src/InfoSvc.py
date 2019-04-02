import json
import falcon
from wsgiref import simple_server

class InfoResource():

    def on_get(self,req,resp):

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"result": "success"})

app = falcon.API()
infoResouceObj = InfoResource()

app.add_route("/info",infoResouceObj)

if __name__ == "__main__":

    httpd = simple_server.make_server('0.0.0.0', 8000, app)
    print("Info api has been started and listening on http://0.0.0.0:8000/info")

    httpd.serve_forever()