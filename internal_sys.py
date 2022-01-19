from selenium.webdriver import Firefox
from time import sleep
from btms import date 
from bs4 import BeautifulSoup


browser = Firefox()
browser.get('https://sistema.bonitour.com.br/login')

login = 'Matheus Bonfim'
senha = '123578951'

campo_login = browser.find_element_by_css_selector('#login')
campo_senha = browser.find_element_by_css_selector('#password')

campo_login_super = browser.find_element_by_css_selector('#login_supervisor')
campo_senha_super = browser.find_element_by_css_selector('#password_supervisor')

campo_login.send_keys(login)
campo_senha.send_keys(senha)
campo_login_super.send_keys(login)
campo_senha_super.send_keys(senha)

button = browser.find_element_by_css_selector('.ui-button')
button.click()
sleep(1)

browser.get('https://sistema.bonitour.com.br/roteiros/movimento_diario')


data = browser.find_element_by_xpath('//*[@id="data"]')
data.click()
data.send_keys(date)

sleep(1)
button_2 = browser.find_element_by_css_selector('.ui-button')
button_2.click()
sleep(1)
req = browser.page_source

soup = BeautifulSoup(req, 'html.parser')

i_par = len(soup.find_all('tr', { 'class' : 'par'}))
i_impar = len(soup.find_all('tr', { 'class' : 'impar'}))
i_impar_det = len(soup.find_all('tr', { 'class' : 'impar_detalhe'}))


for x in range(i_par): 
    print(
        soup.find_all('tr', { 'class' : 'par'})[x].find_all('td')[0].text[9:-8],
        soup.find_all('tr', { 'class' : 'par'})[x].find_all('td')[3].text,
        soup.find_all('tr', { 'class' : 'par'})[x].find_all('td')[4].text[9:-8],
        )

for x in range(i_impar): 
    print(
        soup.find_all('tr', { 'class' : 'impar'})[x].find_all('td')[0].text[9:-8],
        soup.find_all('tr', { 'class' : 'impar'})[x].find_all('td')[3].text,
        soup.find_all('tr', { 'class' : 'impar'})[x].find_all('td')[4].text[9:-8],
        )

for x in range(i_impar_det): 
    print(
        soup.find_all('tr', { 'class' : 'impar_detalhe'})[x].find_all('td')[0].text[9:-8],
        soup.find_all('tr', { 'class' : 'impar_detalhe'})[x].find_all('td')[3].text,
        soup.find_all('tr', { 'class' : 'impar_detalhe'})[x].find_all('td')[4].text[9:-8],
        )
