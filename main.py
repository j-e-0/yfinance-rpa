import yfinance 
import pyautogui 
import pyperclip
import webbrowser
import time
import platform
import os 
from decouple import config

ticker = input('Digite o código da ação: ') 
dados = yfinance.Ticker(ticker).history("6mo")
fechamento = dados.Close 

# Calcs
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento.iloc[-1]

# Email Data
destinatario = config('contact')
assunto = "Análise Diaria"

mensagem = f""" 
Bom dia, 

Segue abaixo as análises da ação {ticker} dos últimos seis meses: 
Cotação máxima: R${round(maxima,2)} 
Cotação mínima: R${round(minima,2)} 
Cotação atual: R${round(atual,2)} 

Atenciosamente, 
Seu nome. 
""" 

# Open Browser
url = 'http://www.gmail.com'

if(platform.system() == "Windows") :
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe -–start-fullscreen --profile-directory="Profile 1" %s'
elif (platform.system() == "Linux") :
    chrome_path = '/usr/bin/google-chrome %s'
elif (platform.system() == "Darwin") :
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome_path).open(url)

# Aguardando abrir Browser
time.sleep(5)

# Configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 2

# Click em novo email
pyautogui.click(x=int(config('new_mail_XPOS')), y=int(config('new_mail_YPOS')))

# Preenchendo o destinatário 
pyperclip.copy(destinatario) 
pyautogui.hotkey("ctrl", "v") 
pyautogui.press("tab")

# Preenchendo o assunto 
pyperclip.copy(assunto) 
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab") 

# Preenchendo a mensagem 
pyperclip.copy(mensagem) 
pyautogui.hotkey("ctrl", "v") 

# Clicar no botão Enviar 
pyautogui.click(x=int(config('send_mail_XPOS')), y=int(config('send_mail_YPOS'))) 

# fechar a aba do gmail 
pyautogui.hotkey("ctrl", "f4") 

# Imprimir mensagem de enviado com sucesso 
print('E-mail enviado com sucesso!')