import mysql.connector


class Database:

    def __init__(self, lista_titulos, lista_links_reais):
        self.lista_titulos = lista_titulos
        self.lista_links_reais = lista_links_reais

    def alimenta_banco(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='googlenews'
        )

        cursor = mydb.cursor()
        sql = 'INSERT INTO news (dia, hora, titulo, link) VALUES (curdate(), curtime(), %s, %s)'

        while len(self.lista_titulos) > 0 and len(self.lista_links_reais) > 0:
            titulo = self.lista_titulos.pop(0)
            link = self.lista_links_reais.pop(0)
            val = (titulo, link)

            cursor.execute(sql, val)

        mydb.commit()
        mydb.close()
