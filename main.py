import flet as ft
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def main(page:ft.Page):
    page.theme_mode = 'dark'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    def iniciar(e):
       navegador = webdriver.Chrome()
       navegador.get("https://www.google.com/")
       time.sleep(2)
       input_pesquisar = navegador.find_element(By.XPATH, "//textarea[@title='Pesquisar']")
       input_pesquisar.send_keys(f"{input_cidade.value} temperatura")
       time.sleep(2)
       input_pesquisar.send_keys(Keys.ENTER)
       temperatura_google = navegador.find_element(By.ID,"wob_tm")
       
       tempertura_c.value = f'de {input_cidade.value}: {temperatura_google.text}°C'
       tempertura_c.update()
       page.update()
       time.sleep(2)
       
       
       
       
    
    
    input_cidade = ft.CupertinoTextField(
        placeholder_text='cidade',
        width=200,
        bgcolor='transparent',
        prefix= ft.Icon(name=ft.Icons.CLOUD,color='white'),
        padding=10
    )
    btn_iniciar = ft.CupertinoButton(
        text='iniciar',
        bgcolor='green',
        color='white',
        width=200,
        on_click=iniciar
        
    )
    
    temperatura_text = ft.Text(
        value=f'Temperatura',
        color='white',
        size=24
    )
    
    tempertura_c = ft.Text(
        color='whiter',
        size=24
    )
    
    
    page.add(
        input_cidade,
        btn_iniciar,
        ft.Row(
            alignment='center',
            controls=[
                temperatura_text,
                tempertura_c
            ]
            )
        
    )
    
ft.app(target=main)