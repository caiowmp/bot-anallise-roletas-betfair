from winotify import Notification, audio
import constantes 

class Mesa:
    def __init__(self):
        self._nome = None
        self._ultimos_resultados = None
        self._nome_croupier = None

    def __init__(self, nome, ultimos_resultados, nome_crupie):
        self.nome = nome
        self.ultimos_resultados = ultimos_resultados
        self.nome_crupie = nome_crupie

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def ultimos_resultados(self):
        return self._ultimos_resultados

    @ultimos_resultados.setter
    def ultimos_resultados(self, value):
        self._ultimos_resultados = value
        while (len(self._ultimos_resultados) > constantes.QUANTIDADE_PADRAO):
            self._ultimos_resultados.pop()

    @property
    def nome_croupier(self):
        return self._nome_croupier

    @nome_croupier.setter
    def nome_croupier(self, value):
        self._nome_croupier = value

    def __str__(self):
        return f"Mesa: {self.nome}, Últimos Resultados: {self.ultimos_resultados}, Crupiê: {self.nome_crupie}"
    
    def verificar_padrao(self):
        resultado = ''
        if self.ultimos_resultados in constantes.NUMEROS_VERMELHOS:
            resultado += 'Números Vermelhos\n'
        if self.ultimos_resultados in constantes.NUMEROS_PRETOS:
            resultado += 'Números Pretos\n'
        if self.ultimos_resultados in constantes.NUMEROS_PARES:
            resultado += 'Números Pares\n'
        if self.ultimos_resultados in constantes.NUMEROS_IMPARES:
            resultado += 'Números Impares\n'
        if self.ultimos_resultados in constantes.NUMEROS_ALTOS:
            resultado += 'Números Altos\n'
        if self.ultimos_resultados in constantes.NUMEORS_BAIXOS:
            resultado += 'Números Baixos\n'
        if resultado != '':
            self.notificar(resultado)

    def notificar(self, entrada: str):
        notificacao = Notification(app_id="Bot BetFair", 
                             title="Entrada Encontrada", 
                             msg="Mesa: " + self.nome + "\nEntrada: " + entrada,
                             duration="long")
        notificacao.set_audio(audio.Default, loop="False")
        notificacao.show()         