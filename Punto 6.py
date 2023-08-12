class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

        self.pica = "Pica"
        self.dimante = "Diamante"
        self.corazones = "Corazones"
        self.trebol = "Trebol"

mi_carta = Carta(2,"de corazones")
print(mi_carta.valor)
print(mi_carta.pinta)        