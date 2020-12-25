import secrets as sc
import requests as rq

class Updater():
    def request(self):
        password = sc.password
        domain = sc.domain
        hosts = sc.hosts
        URL = "https://dynamicdns.park-your-domain.com/update"
        ip = rq.get('https://api.ipify.org').text

        LASTIP = open("lastip.txt", "r").read()

        if ip == LASTIP:
            print("lastip==ip")
            return

        Updater().writeip(ip)

        for x in hosts:
            PARAMS = {
                "host":x,
                "domain":domain,
                "password":password,
                "ip":ip
            }

            rq.get(url=URL, params=PARAMS)
            #print(r.text)

    def writeip(self, lastip):
        f = open("lastip.txt", "w")
        f.write(lastip)
        f.close

app = Updater()
app.request()