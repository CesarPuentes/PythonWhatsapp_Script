from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def save_info():
    nombres_info = nombres.get()
    telefonos_info = str(telefonos.get())
    nombres_info_coma = nombres_info.count(',')
    telefonos_info_coma = telefonos_info.count(',')
    ##verificar que la cantidad de nombres y telefonos ingresados sean iguales
    if (nombres_info_coma == telefonos_info_coma):
        #convertir strings a listas usando coma como el separador
        nombres_list = list(nombres_info.split(','))
        telefonos_list = list(telefonos_info.split(','))
        print(nombres_list)
        autoWhats(nombres_list, telefonos_list)
        return nombres_list, telefonos_list
    else:
        print("Los nombres y números no son iguales")


def autoWhats(nombres, telefonos):
    #Uses Chrome's webdriver avilable in folder and assign it to the variable 'driver'
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://web.whatsapp.com")
    print(nombres)
    #Verificar que el código QR sea ingresado (provisional)
    input("Scan the QR code and then press Enter")
    #assign parameter
    for i in range (len(nombres)):
        driver.get("https://api.whatsapp.com/send?phone=57"+telefonos[i])
        print(telefonos[i])
        element = driver.find_element_by_id('action-button')
        element.click()
        time.sleep(2)
        element = driver.find_element_by_link_text('use WhatsApp Web')
        element.click()
        time.sleep(2)
        #find the chat window and write message
        element = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        element.click()
        element.send_keys('Hola'+ nombres[i] + 'Esto es un mensaje automatico!')
        element.send_keys(Keys.ENTER)
        time.sleep(2)

screen = Tk()
screen.geometry("500x500")
screen.title("Automatizador Whatsapp")
heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()
 
nombres_text = Label(text = "Ingrese nombres separados por comas ",)
telefonos_text = Label(text = "Ingrese teléfonos separados por comas ",)

nombres_text.place(x = 15, y = 70)
telefonos_text.place(x = 15, y = 140)

nombres = StringVar()
telefonos = StringVar()

nombres_entry = Entry(textvariable = nombres, width = "30")
telefonos_entry = Entry(textvariable = telefonos, width = "30")

nombres_entry.place(x = 15, y = 100)
telefonos_entry.place(x = 15, y = 180)

register = Button(screen,text = "Enviar!", width = "30", height = "2", bg = "grey", command = save_info)
register.place(x = 15, y = 290)
