from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from mesa import Mesa
from time import sleep
from winotify import Notification, audio
import constantes

def notificar(mesa: Mesa, entrada: str):
  notificacao = Notification(app_id="Bot BetFair", 
                             title="Entrada Encontrada", 
                             msg="Mesa: " + mesa.nome + "\nEntrada: " + entrada,
                             duration="long")
  notificacao.set_audio(audio.Default, loop="False")
  notificacao.show()


def criarMesas(navegador: ChromeDriverManager):
  div_roletas = navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div[1]')
  pass

# Abrir o navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://identitysso.betfair.com/view/login?product=launcher&redirectMethod=GET&url=https%3A%2F%2Flauncher.betfair.com%2F%3FgameId%3Dlive-rolet-brasileria-cptl%26returnURL%3Dhttps%253A%252F%252Fcasino.betfair.com%252Fpt-br%252Fc%252Fpopular-no-brasil%26launchProduct%3Dgaming%26RPBucket%3Dgaming%26mode%3Dreal%26dataChannel%3Decasino%26switchedToPopup%3Dtrue&regurl=')
sleep(5)

# Fazer login no site
navegador.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]').click()
navegador.find_element('xpath', '//*[@id="username"]').send_keys(constantes.LOGIN)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(constantes.SENHA)
sleep(5)
navegador.find_element('xpath', '//*[@id="loginForm"]/fieldset/div[5]').click()
sleep(10)

# Ir pro site das roletas brasileiras
navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[2]/header/div[3]/div[4]').click()
sleep(5)
navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div[5]').click()
sleep(10)
notificar(Mesa("teste",[],""),"Função feita corretamente")
while True:
  print(navegador.find_element('xpath','//*[@id="root"]/div/div[3]/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div[13]/div/div/div[1]/div/div[3]/div[2]/div/div[1]/div/div'))
