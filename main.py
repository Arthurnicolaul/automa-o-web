import flet as ft
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def main(page: ft.Page):
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def iniciar(e):
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        navegador = webdriver.Chrome(options=chrome_options)
        navegador.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        navegador.get("https://www.google.com/")
        time.sleep(random.randint(2, 5))

        # Movendo o mouse antes de pesquisar
        actions = ActionChains(navegador)
        actions.move_by_offset(random.randint(50, 300), random.randint(50, 300)).perform()
        time.sleep(2)

        input_pesquisar = navegador.find_element(By.XPATH, "//textarea[@title='Pesquisar']")
        input_pesquisar.send_keys(f"{input_cidade.value} temperatura")
        time.sleep(2)
        input_pesquisar.send_keys(Keys.ENTER)

        try:
            temperatura_google = WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.ID, "wob_tm"))
            )
            condicao_tempo = navegador.find_element(By.ID, "wob_dc").text
            umidade = navegador.find_element(By.ID, "wob_hm").text
            vento = navegador.find_element(By.ID, "wob_ws").text

            tempertura_c.value = f"de {input_cidade.value} {temperatura_google.text}°C"
            condicao_clima.value = f"Condição: {condicao_tempo}"
            umidade_text.value = f"Umidade: {umidade}"
            vento_text.value = f"Vento: {vento}"
        except Exception:
            tempertura_c.value = "Erro ao buscar temperatura. Tente novamente."
            condicao_clima.value = ""
            umidade_text.value = ""
            vento_text.value = ""

        tempertura_c.update()
        condicao_clima.update()
        umidade_text.update()
        vento_text.update()
        page.update()
        navegador.quit()
        
    pergunta = ft.Text(value="Deseja ver a temperatura de qual cidade ?", size=24, color="white")

    input_cidade = ft.CupertinoTextField(
        placeholder_text="Cidade",
        width=200,
        bgcolor="transparent",
        prefix=ft.Icon(name=ft.Icons.CLOUD, color="white"),
        padding=10,
    )

    btn_iniciar = ft.CupertinoButton(
        text="Iniciar",
        bgcolor="green",
        color="white",
        width=200,
        on_click=iniciar,
    )

    temperatura_text = ft.Text(value="Temperatura", color="white", size=24)
    tempertura_c = ft.Text(color="white", size=24)
    condicao_clima = ft.Text(color="white", size=24)
    umidade_text = ft.Text(color="white", size=24)
    vento_text = ft.Text(color="white", size=24)

    page.add(
        pergunta,
        input_cidade,
        btn_iniciar,
        ft.Row(alignment="center", controls=[temperatura_text, tempertura_c]),
        ft.Row(alignment="center", controls=[condicao_clima]),
        ft.Row(alignment="center", controls=[umidade_text]),
        ft.Row(alignment="center", controls=[vento_text]),
    )

ft.app(target=main)
