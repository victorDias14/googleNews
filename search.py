import requests
from bs4 import BeautifulSoup


class Search:

    def __init__(self, termos):
        self.termos = termos

    def gera_link_pesquisa(self):
        lista_links = []

        for termos in self.termos:
            link = f'https://news.google.com/search?q={termos}%20when%3A1h&hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
            lista_links.append(link)

        return lista_links

    @staticmethod
    def gera_links_relativos_titulo_noticia(lista_links):

        lista_links_relativos = []
        lista_titulo_noticia = []

        for x in lista_links:
            pagina = requests.get(x)
            codhtml = BeautifulSoup(pagina.content, 'html.parser')

            for y in codhtml.find_all('a'):
                link_relativo = y.get('href')

                if type(link_relativo) == str:
                    filtro = link_relativo[2:10]

                    if filtro == 'articles':
                        lista_links_relativos.append(link_relativo[1:])

                        titulo_noticia = y.get_text('href')

                        if titulo_noticia != '':
                            lista_titulo_noticia.append(titulo_noticia)

        return lista_links_relativos, lista_titulo_noticia

    @staticmethod
    def gera_link_real(lista_links_relativos):
        lista_links_reais = []

        while len(lista_links_relativos) > 0:
            link_relativo_completo = 'https://news.google.com' + lista_links_relativos.pop(0)
            r = requests.get(link_relativo_completo).url
            lista_links_reais.append(r)
            del lista_links_relativos[0:2]

        return lista_links_reais

