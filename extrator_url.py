import re


class ExtratorURL():
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URl está vazia")

        padrao_url = re.compile('(http[s]?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogação = self.url.find("?")
        url_base = self.url[:indice_interrogação]
        return url_base

    def get_url_parametros(self):
        indice_interrogação = self.url.find("?")
        url_paramentros = self.url[(indice_interrogação + 1):]
        return url_paramentros

    def get_valor_parametro(self, paramentro_busca):
        indice_parametro = self.get_url_parametros().find(paramentro_busca)
        indice_valor = indice_parametro + len(paramentro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print(extrator_url == extrator_url_2)
print(extrator_url)

valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

dolar = (int(quantidade) / valor_dolar)
print(type(dolar))
print("{}".format("%.2f" % dolar))



































