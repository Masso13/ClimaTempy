import requests, json

class ClimaTempo(object):
    def __init__(self, cidade):
        self.cidade = cidade
        self.clima = None
        self.dados = None

        self.pegarDados()
        self.pegarClima()

    def pegarDados(self):
        self.dados = json.loads(requests.post("https://www.climatempo.com.br/json/busca-por-nome", data={"name": self.cidade}).text)[0]["response"]["data"][0]

    def pegarClima(self):
        idlocale = str(self.dados["idlocale"])
        resposta = json.loads(requests.post("https://www.climatempo.com.br/json/myclimatempo/user/weatherNow?idlocale="+idlocale).text)[0]["data"][0]["weather"][0]
        self.clima = {i: v for (i,v) in resposta.items() if i != "icon"}