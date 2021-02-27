import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
from pathlib import Path

cwd = os.getcwd()
xoli = f'{cwd}'.replace(' \ '.strip(), ('/') )
xoli = xoli + '/geckodriver.exe'

class telaPython:
    def __init__(self):
        # -----------Layote--------------
        sg.ChangeLookAndFeel('DarkBrown4')
        self.layote = [[sg.Text('Usuário:'), sg.Input(key='Usuário')],
                       [sg.Text('Senha: '), sg.Input(key='Senha',password_char='*')],
                       [sg.Text('Tag:    ',size=(5,0)), sg.Input(key='tag')],
                       [sg.Button('enviar')]]

        self.layote2 = [[sg.Text('Digite os comentarios de sua preferência')],
                        [sg.Text('Comentário 1: '), sg.Input(key='comentário1')],
                        [sg.Text('Comentário 2: '), sg.Input(key='comentário2')],
                        [sg.Text('Comentário 3: '), sg.Input(key='comentário3')],
                        [sg.Text('Comentário 4: '), sg.Input(key='comentário4')],
                        [sg.Text('Comentário 5: '), sg.Input(key='comentário5')],
                        [sg.Button('Enviar')]]

        # -----------Janelas--------------
        self.janela = sg.Window('Dados do usuário',size=(400,130)).layout(self.layote)
        self.janela2 = sg.Window('comentario 1: ',size=(400,200)).layout(self.layote2)
        # --------Extrair os dados-----------
    @property
    def iniciar(self):
        self.button, self.values = self.janela.Read()
        usuario = self.values['Usuário']
        senha = self.values['Senha']
        tag = self.values['tag']
        y = [usuario, senha, tag]
        print(self.values)
        return y

    @property
    def iniciar2(self):
        self.button, self.values = self.janela2.Read()
        comentário1 = self.values['comentário1']
        comentário2 = self.values['comentário2']
        comentário3 = self.values['comentário3']
        comentário4 = self.values['comentário4']
        comentário5 = self.values['comentário5']
        x = [comentário1,comentário2,comentário3,comentário4,comentário5]
        print(self.values)
        return x

class instragamBot:
    def __init__(self, usuario, senha, tag, listax2, cwd):
        self.usuario = usuario
        self.senha = senha
        self.tag = tag
        self.listax2 = listax2
        xoli = f'{cwd}'.replace(' \ '.strip(), ('/') )
        xoli = xoli + '/geckodriver.exe'
        self.driver = webdriver.Firefox(executable_path=xoli)
        self.contador = 1

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
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2,5))
                self.digite_como_humano(random.choice(self.listax2),campo_comentario)
                time.sleep(random.randint(30,120))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                self.contador = self.contador + 1

            except Exception as e:
                print(e)
                print(self.contador)

tela = telaPython()
x = tela.iniciar
nome = x[0]
senha = x[1]
tag = x[2]
x2list = tela.iniciar2
bot = instragamBot(nome,senha,tag,x2list,cwd)
bot.login()