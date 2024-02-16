from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from mesa import Mesa
from time import sleep
import constantes

def criarMesas(navegador: webdriver.Chrome, nomes_das_mesas, nomes_dos_croupier):
  contador = 0
  total_de_resultados_anteriores = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'roulette-history-item__value-text--siwxW')]
  resultados = []

  for resultados_passados in total_de_resultados_anteriores:
    resultados.append(resultados_passados)
    if(len(resultados) == 9):
      if("Auto Roulette" not in nomes_dos_croupier[contador] and nomes_dos_croupier[contador] != nomes_dos_croupier[contador-1]):
        mesas.append(Mesa(nomes_das_mesas[contador],resultados,nomes_dos_croupier[contador]))
        mesas[-1].verificar_padrao()
      contador += 1
      resultados = []

def atualizarMesas(navegador: webdriver.Chrome, nomes_das_mesas, nomes_dos_croupier):
  contador = 0
  total_de_resultados_anteriores = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'roulette-history-item__value-text--siwxW')]
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
  global nomes_das_mesas
  global nomes_dos_croupier
  try:
    if len(mesas) == 0:
      criarMesas(navegador,nomes_das_mesas,nomes_dos_croupier)
    else:
      atualizarMesas(navegador,nomes_das_mesas,nomes_dos_croupier)
  except:
    navegador.refresh()

def abrir_navegador():
  global navegador
  servico = Service(ChromeDriverManager().install())
  navegador = webdriver.Chrome(service=servico)
  navegador.get('https://identitysso.betfair.com/view/login?product=launcher&redirectMethod=GET&url=https%3A%2F%2Flauncher.betfair.com%2F%3FgameId%3Dlive-rolet-brasileria-cptl%26returnURL%3Dhttps%253A%252F%252Fcasino.betfair.com%252Fpt-br%252F%26launchProduct%3Dgaming%26RPBucket%3Dgaming%26mode%3Dreal%26dataChannel%3Decasino%26switchedToPopup%3Dtrue&regurl=')
  sleep(5)

def ir_para_login():
  global navegador
  navegador.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]').click()

def fazer_login():
  global navegador
  navegador.find_element('xpath', '//*[@id="username"]').send_keys(constantes.LOGIN)
  navegador.find_element('xpath', '//*[@id="password"]').send_keys(constantes.SENHA)
  sleep(10)
  navegador.find_element('xpath', '//*[@id="loginForm"]/fieldset/div[5]').click()
  sleep(10)

def ir_para_roletas():
  global navegador
  navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div[2]/header/div[3]/div[4]').click()
  sleep(10)
  navegador.find_element('xpath', '//*[@id="root"]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div[5]').click()
  sleep(10)
  
constantes.exibir_notificacao()
print(constantes.QUANTIDADE_PADRAO)
abrir_navegador()
ir_para_login()
fazer_login()
ir_para_roletas()
mesas = []
nomes_das_mesas =  [div.text for div in navegador.find_elements(By.CLASS_NAME, 'table-footer__name--BJPlO')]
nomes_dos_croupier = [div.text for div in navegador.find_elements(By.CLASS_NAME, 'table__dealer-name-text--uO9ri')]

while True:
  atualizarOuCriarMesas()