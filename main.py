import search
import database

termo = str
listaTermos = []

while True:
    termo = input('Informe o termo que deseja pesquisar ou pressione Enter para continuar: ')

    if termo != '':
        listaTermos.append(termo)

    else:
        break

busca = search.Search(listaTermos)

listaLinks = busca.gera_link_pesquisa()

listaLinksRelativosTitulos = busca.gera_links_relativos_titulo_noticia(listaLinks)
listaLinksRelativos = listaLinksRelativosTitulos[0]
listaTitulos = listaLinksRelativosTitulos[1]

listaLinksReais = busca.gera_link_real(listaLinksRelativos)

banco = database.Database(listaTitulos, listaLinksReais)
banco.alimenta_banco()
