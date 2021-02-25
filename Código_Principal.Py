import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class telaPython:
    def __init__(self):
        # -----------Layote--------------
        sg.ChangeLookAndFeel('DarkBrown4')
        self.layote = [[sg.Text('Usuário:'), sg.Input(key='Usuário')],
                       [sg.Text('Senha: '), sg.Input(key='Senha',password_char='*')],
                       [sg.Text('Tag:    ',size=(5,0)), sg.Input(key='tag')],
                       [sg.Button('enviar')]]


        # -----------Janela--------------
        self.janela = sg.Window('Dados do usuário',size=(400,130)).layout(self.layote)

        # --------Extrair os dados-----------
    def iniciar(self):
        self.button, self.values = self.janela.Read()
        usuario = self.values['Usuário']
        senha = self.values['Senha']
        tag = self.values['tag']
        y = [usuario, senha, tag]
        print(self.values)
        return y

class instragamBot:
    def __init__(self, usuario, senha, tag):
        self.usuario = usuario
        self.senha = senha
        self.tag = tag
        self.driver = webdriver.Firefox(executable_path="C:/Users/multa/PycharmProjects/TesteInterface/geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        botão_nome = driver.find_element_by_xpath("//input[@name='username']")
        botão_nome.click()
        botão_nome.clear()
        botão_nome.send_keys(self.usuario)

        botão_senha = driver.find_element_by_xpath("//input[@name='password']")
        botão_senha.click()
        botão_senha.clear()
        botão_senha.send_keys(self.senha)
        botão_senha.send_keys(Keys.RETURN)
        time.sleep(3)
        self.comente_nas_fotos(f'{self.tag}')

    @staticmethod
    def digite_como_humano(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comente_nas_fotos(self,hashtag):
        driver = self.driver
        driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrfs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrfs if hashtag in href]
        print(f'{hashtag} fotos {str(len(pic_hrfs))}')

        for pic_hrfs in pic_hrfs:
            driver.get(pic_hrfs)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                comentarios = ['Wooow','Incrível','massa!!','Que demais']
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2,5))
                self.digite_como_humano(random.choice(comentarios),campo_comentario)
                time.sleep(random.randint(30,120))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(5)

            except Exception as e:
                print(e)


tela = telaPython()
x = tela.iniciar()
nome = x[0]
senha = x[1]
tag = x[2]
bot = instragamBot(nome,senha,tag)
bot.login()