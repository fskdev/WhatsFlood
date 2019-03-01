from selenium import webdriver
from tkinter import *
import os

def janelaMain():

    def floodar():

        driver = webdriver.Chrome("requisitos/chromedriver.exe")
        driver.get("https://web.whatsapp.com/")

        nome = str(eNome.get())
        mensagem = str(eMensagem.get())
        quantidade = int(eQuantidade.get())

        os.system("cls")
        input("Aperte ENTER quando o QR Code for verificado")

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
        user.click()

        msg_box = driver.find_element_by_class_name("_1Plpp")

        os.system("cls")
        print("Flood em andamento......")

        def loop():
            for i in range(quantidade):
                msg_box.send_keys(mensagem)
                button = driver.find_element_by_class_name("_35EW6")
                button.click()
        loop()
        print("Flood finalizado com sucesso!")




    FloodWindow = Tk()
    FloodWindow.geometry("300x200+500+100")
    FloodWindow.title("Whats Flood")
    FloodWindow.resizable(False, False)
    FloodWindow.configure(bg="black")

    tWhatsFlood = Label(FloodWindow, text="WHATS FLOOD", bg="black", fg="red", font="Verdana 13")
    tWhatsFlood.pack()

    tNome = Label(FloodWindow, text="Nome do contato", bg="black", fg="white", font="Verdana 10")
    tNome.pack()

    eNome = Entry(FloodWindow, width=25)
    eNome.pack()

    tMensagem = Label(FloodWindow, text="Mensagem", bg="black", fg="white", font="Verdana 10")
    tMensagem.pack()

    eMensagem = Entry(FloodWindow, width=25)
    eMensagem.pack()

    tQuantidade = Label(FloodWindow, text="Quantidade", bg="black", fg="white", font="Verdana 10")
    tQuantidade.pack()

    eQuantidade = Entry(FloodWindow, width=25)
    eQuantidade.pack()

    bFloodar = Button(FloodWindow, text="Floodar", bg="black", fg="white", width=30, command = lambda: floodar())
    bFloodar.place(x=40,y=165)

    FloodWindow.mainloop()

janelaMain()
