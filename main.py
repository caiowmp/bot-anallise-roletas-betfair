from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
  global mesas
  contador = 0
  total_de_resultados_anteriores = navegador.find_elements(By.CLASS_NAME, 'roulette-history-item__value-text--siwxW')
  # print(len(total_de_resultados_anteriores))
  nomes_das_mesas = navegador.find_elements(By.CLASS_NAME, 'table-footer__name--BJPlO')
  nomes_dos_croupier = navegador.find_elements(By.CLASS_NAME, 'table__dealer-name-text--uO9ri')
  resultados = []
  for resultados_passados in total_de_resultados_anteriores:
    # print(resultados_passados.text)
    # if(resultados_passados.text is not None):
    resultados.append(resultados_passados.text)
    if(len(resultados) == 9):
      # print(contador)
      if("Auto Roulette" not in nomes_dos_croupier[contador].text and nomes_dos_croupier[contador].text != nomes_dos_croupier[contador-1].text):
        mesas.append(Mesa(nomes_das_mesas[contador].text,resultados,nomes_dos_croupier[contador].text))
        print(mesas[-1].__str__())
      contador += 1
      resultados = []
  print("Fim criação")

def atualizarMesas(navegador: ChromeDriverManager):
  print("Incio atualizacao")
  global mesas
  contador = 0
  total_de_resultados_anteriores = navegador.find_elements(By.CLASS_NAME, 'roulette-history-item__value-text--siwxW')
  nomes_das_mesas = navegador.find_elements(By.CLASS_NAME, 'table-footer__name--BJPlO')
  nomes_dos_croupier = navegador.find_elements(By.CLASS_NAME, 'table__dealer-name-text--uO9ri')
  resultados = []
  for resultados_passados in total_de_resultados_anteriores:
    resultados.append(resultados_passados.text)
    if(len(resultados) == 9):
      # print(contador)
      if("Auto Roulette" not in nomes_dos_croupier[contador].text and nomes_dos_croupier[contador].text != nomes_dos_croupier[contador-1].text):
        for mesa in mesas:
          if mesa.nome == nomes_das_mesas[contador].text:
            mesa.ultimos_resultados.append(resultados[-1])
            print(mesa.__str__())      
      contador += 1
      resultados = []

def atualizarOuCriarMesas(navegador: ChromeDriverManager):
  if len(mesas) == 0:
    criarMesas(navegador)
  else:
    atualizarMesas(navegador)

mesas = []

# Abrir o navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://identitysso.betfair.com/view/login?product=launcher&redirectMethod=GET&url=https%3A%2F%2Flauncher.betfair.com%2F%3FgameId%3Dlive-rolet-brasileria-cptl%26returnURL%3Dhttps%253A%252F%252Fcasino.betfair.com%252Fpt-br%252Fc%252Fpopular-no-brasil%26launchProduct%3Dgaming%26RPBucket%3Dgaming%26mode%3Dreal%26dataChannel%3Decasino%26switchedToPopup%3Dtrue&regurl=')
sleep(5)

# Fazer login no site
navegador.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]').click()
navegador.find_element('xpath', '//*[@id="username"]').send_keys(constantes.LOGIN)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(constantes.SENHA)
sleep(7)
navegador.find_element('xpath', '//*[@id="loginForm"]/fieldset/div[5]').click()
sleep(10)

# Ir pro site das roletas brasileiras
navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[2]/header/div[3]/div[4]').click()
sleep(5)
navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div[5]').click()
sleep(10)
while True:
  # try:
    atualizarOuCriarMesas(navegador)
    sleep(30)
  # except:
  #   print(1)