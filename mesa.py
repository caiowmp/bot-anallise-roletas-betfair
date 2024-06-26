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
        while (len(self._ultimos_resultados) > constantes.QUANTIDADE_PADRAO):
            self._ultimos_resultados.pop()
        return self._ultimos_resultados

    @ultimos_resultados.setter
    def ultimos_resultados(self, value):
        self._ultimos_resultados = value

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
        if all(numero in constantes.NUMEROS_VERMELHOS for numero in self.ultimos_resultados):
            resultado += 'Números Vermelhos\n'
        if all(numero in constantes.NUMEROS_PRETOS for numero in self.ultimos_resultados):
            resultado += 'Números Pretos\n'
        if all(numero in constantes.NUMEROS_PARES for numero in self.ultimos_resultados):
            resultado += 'Números Pares\n'
        if all(numero in constantes.NUMEROS_IMPARES for numero in self.ultimos_resultados):
            resultado += 'Números Impares\n'
        if all(numero in constantes.NUMEROS_ALTOS for numero in self.ultimos_resultados):
            resultado += 'Números Altos\n'
        if all(numero in constantes.NUMEORS_BAIXOS for numero in self.ultimos_resultados):
            resultado += 'Números Baixos\n'
        if resultado != '':
            self.notificar(resultado)

    def notificar(self, entrada: str):
        notificacao = Notification(app_id="Bot BetFair", 
                             title="Entrada Encontrada", 
                             msg="Mesa: " + self.nome + "\nEntrada: " + entrada,
                             duration="short")
        notificacao.set_audio(audio.Default, loop="False")
        notificacao.show()
        print("Notifiquei", self.__str__())
        self.ultimos_resultados = [-1]  

    # def verificar_padrao_vermelho(self):
    #     contador = 0
    #     for numero in self.ultimos_resultados:
    #         if numero in constantes.NUMEROS_VERMELHOS:
    #             contador += 1
    #     return contador == constantes.QUANTIDADE_PADRAO
    
    # def verificar_padrao_preto(self):
    #     contador = 0
    #     for numero in self.ultimos_resultados:
    #         if numero in constantes.NUMEROS_PRETOS:
    #             contador += 1
    #     return contador == constantes.QUANTIDADE_PADRAO
    
    # def verificar_padrao_par(self):
    #     contador = 0
    #     for numero in self.ultimos_resultados:
    #         if numero in constantes.NUMEROS_PARES:
    #             contador += 1
    #     return contador == constantes.QUANTIDADE_PADRAO
    
    # def verificar_padrao_impar(self):
    #     contador = 0
    #     for numero in self.ultimos_resultados:
    #         if numero in constantes.NUMEROS_IMPARES:
    #             contador += 1
    #     return contador == constantes.QUANTIDADE_PADRAO
    
    # def verificar_padrao_baixo(self):
    #     contador = 0
    #     for numero in self.ultimos_resultados:
    #         if numero in constantes.NUMEORS_BAIXOS:
    #             contador += 1
    #     return contador == constantes.QUANTIDADE_PADRAO
    
    # def verificar_padrao_alto(self):
    #     contador = 0
    #     for numero in self.ultimos_resultados:
    #         if numero in constantes.NUMEROS_ALTOS:
    #             contador += 1
    #     return contador == constantes.QUANTIDADE_PADRAO

    # def notificar(self, entrada: str):
    #     notificacao = ToastNotifier()
    #     notificacao.show_toast("Entrada encontrada", 
    #                            "Mesa: " + self.nome + "\nEntrada: " + entrada, 
    #                            duration=10)
    #     print("Notifiquei mesmo!", self.__str__())
    #     self.ultimos_resultados = [-1]  

    # def notificar(self, entrada: str):
    #     notification.notify(
    #         title="Entrada encontrada",
    #         message="Mesa: " + self.nome + "\nEntrada: " + entrada, 
    #         app_name="Bot BetFair", 
    #         timeout=10, 
    #     )
    #     print("Notifiquei mesmo!", self.__str__())
    #     self.ultimos_resultados = [-1]    