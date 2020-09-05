import requests
from bs4 import BeautifulSoup


def run():
    # hago la consulta a la pagina con la funcion get de request.
    response = requests.get('https://www.carrefour.com.ar/gaming.html')
    soup = BeautifulSoup(response.content, 'html.parser')

    # con find_all puedo buscar parametros.
    # acá traigo p y tittle y luego extraigo el texto de tittle.
    texto = soup.find_all('p',class_='title')
    precio = soup.find_all('p',class_='price')

    #adjunto el texto a una lista para poder iterarla.
    lista_texto = []
    for x in texto:
        # con un bucle extraigo el texto.
        lista_texto.append(x.text)
    #print(lista_texto)

    # separo y filtro por el precio
    lista_precio = []
    for i in precio:
        lista_precio.append(i.text)

    #Adjunto ambas listas en un diccionario
    diccio = {}
    for adjunt_diccio in range(len(lista_texto)):
        diccio[lista_texto[adjunt_diccio]] = lista_precio[adjunt_diccio]
    for oso in diccio:
        # Separo por palabras para encontrar los mouse
        for lobo in oso.split(' '):
            if lobo == 'Mouse':
                # imprimo el mouse
                print(oso,'->', diccio[oso])

    input()


if __name__ == '__main__':
    run()
