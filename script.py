from bs4 import BeautifulSoup
import requests

lista = []
cartel_l = []
peso_l = []
atletas_l = []
count = 0
pesos_null = []
count2 = 0
count3 = 0



while count < 226:
    response = requests.get(f"https://www.ufc.com.br/athletes/all?gender=All&search=&page={count}")
    page = response.text
    soup = BeautifulSoup(page, "html.parser")

    span = soup.find_all(name='span', class_='c-listing-athlete__title')
    atletas = soup.findAll(name='span', class_='c-listing-athlete__name')
    carteis = soup.find_all(name='span', class_='c-listing-athlete__record')
    pesos = soup.find_all(name='div', class_='field field--name-stats-weight-class field--type-entity-reference field--label-hidden field__items')


    for n in span:
        if n.text == "" or n.text == " ":
            count2 += 1
            count3 += 1
            pesos_null.append(count3)
        else:
            count3 += 1


    for n in carteis:
        cartel = n.text
        cartel_l.append(cartel)

    for n in atletas:
        atletas = n.text.replace('\n','').replace('        ',"")
        lista.append(atletas)

    for n in pesos:
        pesos = n.text.replace('\n',"")
        peso_l.append(pesos)


    count += 1
    print(count)

count1 = 0

for n in  range (0,len(lista),2):
    atletas_l.append(lista[n])

for n in pesos_null:
    peso_l.insert(n - 1,"Null")

lutadores = {
    'nome':"",
    'peso':"",
    'cartel':""
}

lutadores = []

for n in range (0,len(atletas_l)):
    obj = {
     'nome':atletas_l[n],
     'peso': peso_l[n],
     'cartel': cartel_l[n]
    }
    lutadores.append(obj)

with open('lutadores.txt', mode='w', encoding='utf-8') as file:
    for lutador in lutadores:
        file.write(f"Nome:{lutador['nome']}\nCatégoria:  {lutador['peso']}\nCartel:  {lutador['cartel']}\n\n")