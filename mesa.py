from constantes import QUANTIDADE_PADRAO

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
        if(len(self._ultimos_resultados) > QUANTIDADE_PADRAO):
            self._ultimos_resultados.pop(0)

    @property
    def nome_croupier(self):
        return self._nome_croupier

    @nome_croupier.setter
    def nome_croupier(self, value):
        self._nome_croupier = value

    def __str__(self):
        return f"Mesa: {self.nome}, Últimos Resultados: {self.ultimos_resultados}, Crupiê: {self.nome_crupie}"