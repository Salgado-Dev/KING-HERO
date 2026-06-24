import os
import time
import random
import string
import logging
import json
import hashlib
import base64
import threading
import subprocess
import sys
import platform
import shutil
import glob
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *


logging.basicConfig(filename='painel_hacker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if os.name == 'nt':
    os.system('color 0a')
    os.system('cls')

ASCII_ART = r"""
██╗  ██╗██╗███╗   ██╗ ██████╗
██║ ██╔╝██║████╗  ██║██╔════╝
█████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
"""

print(ASCII_ART)
print("=== PAINEL HACKER v8.0 - VERSÃO EXPANDIDA ===\n")


def log_info(msg):
    logging.info(msg)
    print(f"[+] {msg}")

def log_erro(msg):
    logging.error(msg)
    print(f"[!] {msg}")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_email():
    return f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}{random.randint(100,999)}@gmail.com"

def gerar_senha_forte(tamanho=28):
    chars = string.ascii_letters + string.digits + "@#"
    senha = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.choice(string.digits), "@"]
    senha.extend(random.choices(chars, k=tamanho-4))
    random.shuffle(senha)
    return ''.join(senha)

def salvar_credencial(site, email, senha):
    with open("credenciais_hacker.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{site}] {email} | {senha}\n")

def salvar_senhas(quantidade=500):
    with open("senhas_fortes.txt", "w", encoding="utf-8") as f:
        for _ in range(quantidade):
            f.write(gerar_senha_forte(30) + "\n")
    log_info(f"{quantidade} senhas geradas!")

def criar_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def aplicar_fuck_system(driver):
    log_info("Aplicando KING SYSTEM...")
    time.sleep(1.5)
    try:
        driver.execute_script("document.body.innerHTML = '';")
        driver.execute_script(f"""
            let d = document.createElement('div');
            d.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:#000;display:flex;align-items:center;justify-content:center;z-index:99999999;font-family:monospace;font-size:17px;line-height:0.9;color:#00ff00;white-space:pre;';
            d.textContent = `{ASCII_ART}`;
            document.body.appendChild(d);
        """)
    except:
        pass

def tentar_nao_sou_robo(driver):
    log_info("Tentando resolver reCAPTCHA...")
    time.sleep(random.uniform(2.5, 5))
    try:
        for iframe in driver.find_elements(By.TAG_NAME, "iframe"):
            if "recaptcha" in (iframe.get_attribute("src") or ""):
                driver.switch_to.frame(iframe)
                checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'recaptcha-checkbox')]")))
                checkbox.click()
                log_info("reCAPTCHA resolvido!")
                time.sleep(4)
                driver.switch_to.default_content()
                return True
    except:
        pass
    return False


def fuck_key_gmail(driver):
    log_info("King Key Gmail iniciado")
    tentar_nao_sou_robo(driver)
    try:
        email = gerar_email()
        senha = gerar_senha_forte(30)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "identifierId"))).send_keys(email)
        driver.find_element(By.XPATH, "//button").click()
        time.sleep(4)
        WebDriverWait(driver, 12).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys(senha)
        salvar_credencial("Gmail", email, senha)
        log_info(f"Email: {email} | Senha: {senha}")
    except:
        log_erro("Erro no Gmail")

def fuck_key_facebook(driver):
    log_info("King key Facebook iniciado")
    tentar_nao_sou_robo(driver)
    try:
        email = gerar_email()
        senha = gerar_senha_forte(30)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(senha)
        salvar_credencial("Facebook", email, senha)
        log_info("Campos preenchidos no Facebook")
    except:
        log_erro("Erro no Facebook")

def fuck_key_roblox(driver):
    log_info("King key Roblox iniciado")
    tentar_nao_sou_robo(driver)
    try:
        email = gerar_email()
        senha = gerar_senha_forte(30)
        driver.find_element(By.NAME, "username").send_keys(email)
        log_info("Username preenchido no Roblox")
    except:
        log_erro("Erro no Roblox")

def fuck_key_generico(driver):
    log_info("Fuck Key Genérico iniciado")
    tentar_nao_sou_robo(driver)
    try:
        email = gerar_email()
        senha = gerar_senha_forte(30)
        for sel in ["input[type='email']", "#identifierId", "input[name*='email']", "input[type='text']"]:
            try:
                campo = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, sel)))
                if campo.is_displayed():
                    campo.send_keys(email)
                    break
            except:
                continue
        try:
            campo_senha = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
            campo_senha.send_keys(senha)
            salvar_credencial("Site Genérico", email, senha)
        except:
            pass
    except:
        log_erro("Erro Genérico")


def abrir_abas_massa(driver, qtd=50):
    sites = ["https://www.youtube.com", "https://twitter.com", "https://www.instagram.com", "https://www.twitch.tv", "https://github.com"]
    for _ in range(qtd):
        driver.execute_script(f"window.open('{random.choice(sites)}', '_blank');")
        time.sleep(0.1)
    log_info(f"{qtd} abas abertas")

def bombardeio_google(driver, qtd=30):
    termos = ["hacking", "deep web", "roblox hack", "leak 2026", "dark web"]
    for _ in range(qtd):
        driver.get("https://www.google.com")
        try:
            driver.find_element(By.NAME, "q").send_keys(random.choice(termos) + Keys.RETURN)
            time.sleep(random.uniform(2.5, 5))
        except:
            pass
    log_info("Bombardeio concluído")

def auto_scroll_max(driver):
    for _ in range(25):
        driver.execute_script("window.scrollBy(0, 5000);")
        time.sleep(1.2)
    log_info("Scroll máximo executado")

def limpar_tudo(driver):
    driver.delete_all_cookies()
    driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    log_info("Todos os dados limpos")

def screenshot_html(driver):
    ts = datetime.now().strftime("%H%M%S")
    driver.save_screenshot(f"hack_{ts}.png")
    with open(f"pagina_{ts}.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    log_info("Screenshot e HTML salvos")

def mostrar_menu():
    print("\n" + "="*80)
    print("               PAINEL HACKER v8.0")
    print("="*80)
    print("1  - KING ALL")
    print("2  - KING key Gmail")
    print("3  - KING key Genérico")
    print("4  - KING key Facebook")
    print("5  - KING key Roblox")
    print("6  - Auto Não Sou Robô")
    print("7  - Abrir Abas em Massa")
    print("8  - Bombardeio Google")
    print("9  - Auto Scroll Máximo")
    print("10 - Limpar Dados")
    print("11 - Screenshot + HTML")
    print("12 - Gerar Senhas Fortes")
    print("0  - Sair")
    print("="*80)



while True:
    limpar_tela()
    print(ASCII_ART)
    mostrar_menu()
    
    op = input("\nEscolha: ").strip()

    if op == "0":
        print("Saindo...")
        break

    driver = criar_driver()

    try:
        if op == "1":
            driver.get("https://www.google.com")
            aplicar_fuck_system(driver)
        elif op == "2":
            driver.get("https://accounts.google.com/signin")
            fuck_key_gmail(driver)
        elif op == "3":
            url = input("URL: ") or "https://www.google.com"
            driver.get(url)
            fuck_key_generico(driver)
        elif op == "4":
            driver.get("https://www.facebook.com")
            fuck_key_facebook(driver)
        elif op == "5":
            driver.get("https://www.roblox.com")
            fuck_key_roblox(driver)
        elif op == "6":
            url = input("URL: ") or "https://www.google.com"
            driver.get(url)
            tentar_nao_sou_robo(driver)
        elif op == "7":
            driver.get("https://www.google.com")
            abrir_abas_massa(driver, 50)
        elif op == "8":
            driver.get("https://www.google.com")
            bombardeio_google(driver, 30)
        elif op == "9":
            driver.get("https://www.google.com")
            auto_scroll_max(driver)
        elif op == "10":
            driver.get("https://www.google.com")
            limpar_tudo(driver)
        elif op == "11":
            driver.get("https://www.google.com")
            screenshot_html(driver)
        elif op == "12":
            salvar_senhas(500)
        else:
            print("Opção inválida!")

        input("\nPressione ENTER para continuar...")

    except Exception as e:
        log_erro(f"Erro: {e}")
    finally:
        driver.quit()