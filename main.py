import secrets as sc
import requests as rq

class Updater():
    def request(self):
        password = sc.password
        domain = sc.domain
        hosts = sc.hosts
        URL = "https://dynamicdns.park-your-domain.com/update"
        ip = rq.get('https://api.ipify.org').text

        for x in hosts:
            PARAMS = {
                "host":x,
                "domain":domain,
                "password":password,
                "ip":ip
            }

            rq.get(url=URL, params=PARAMS)
            #print(r.text)

app = Updater()
app.request()