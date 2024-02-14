from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from apscheduler.schedulers.background import BackgroundScheduler
from mesa import Mesa
from time import sleep
import constantes

def criarMesas(navegador: ChromeDriverManager):
  contador = 0
  total_de_resultados_anteriores = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'roulette-history-item__value-text--siwxW')]
  nomes_das_mesas =  [div.text for div in navegador.find_elements(By.CLASS_NAME, 'table-footer__name--BJPlO')]
  nomes_dos_croupier = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'table__dealer-name-text--uO9ri')]
  resultados = []

  for resultados_passados in total_de_resultados_anteriores:
    resultados.append(resultados_passados)
    if(len(resultados) == 9):
      if("Auto Roulette" not in nomes_dos_croupier[contador] and nomes_dos_croupier[contador] != nomes_dos_croupier[contador-1]):
        mesas.append(Mesa(nomes_das_mesas[contador],resultados,nomes_dos_croupier[contador]))
      contador += 1
      resultados = []

def atualizarMesas(navegador: ChromeDriverManager):
  contador = 0
  total_de_resultados_anteriores = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'roulette-history-item__value-text--siwxW')]
  nomes_das_mesas =  [div.text for div in navegador.find_elements(By.CLASS_NAME, 'table-footer__name--BJPlO')]
  nomes_dos_croupier = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'table__dealer-name-text--uO9ri')]
  resultados = []

  for resultados_passados in total_de_resultados_anteriores:
    resultados.append(resultados_passados)
    if(len(resultados) == 9 and "Auto Roulette" not in nomes_dos_croupier[contador] and nomes_dos_croupier[contador] != nomes_dos_croupier[contador-1]):
      for mesa in mesas:
        if mesa.nome == nomes_das_mesas[contador] and resultados[0] != mesa.ultimos_resultados[0]:
          mesa.ultimos_resultados.insert(0, resultados[0])
          mesa.verificar_padrao()
      contador += 1
      resultados = []

def atualizarOuCriarMesas():
  global navegador
  try:
    if len(mesas) == 0:
      criarMesas(navegador)
    else:
      atualizarMesas(navegador)
  except:
    atualizarOuCriarMesas()

mesas = []

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://identitysso.betfair.com/view/login?product=launcher&redirectMethod=GET&url=https%3A%2F%2Flauncher.betfair.com%2F%3FgameId%3Dlive-rolet-brasileria-cptl%26returnURL%3Dhttps%253A%252F%252Fcasino.betfair.com%252Fpt-br%252Fc%252Fpopular-no-brasil%26launchProduct%3Dgaming%26RPBucket%3Dgaming%26mode%3Dreal%26dataChannel%3Decasino%26switchedToPopup%3Dtrue&regurl=')
sleep(5)

navegador.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]').click()
navegador.find_element('xpath', '//*[@id="username"]').send_keys(constantes.LOGIN)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(constantes.SENHA)
sleep(10)
navegador.find_element('xpath', '//*[@id="loginForm"]/fieldset/div[5]').click()
sleep(10)

navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[2]/header/div[3]/div[4]').click()
sleep(5)
navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div[5]').click()
sleep(10)

scheduler = BackgroundScheduler()
scheduler.add_job(navegador.refresh, 'interval', minutes=10)
scheduler.start()

while True:
  atualizarOuCriarMesas()