class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron {cantidad} en la cuenta {self.numero_cuenta}. Nuevo balance: {self.balance}")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta {self.numero_cuenta}. Nuevo balance: {self.balance}")
        else:
            print("Fondos insuficientes para realizar el retiro.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2% en la cuenta {self.numero_cuenta}. Nuevo balance: {self.balance}")

    def mostrar_detalles(self):
        print(f"Detalles de la cuenta {self.numero_cuenta}:")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: {self.balance}")

cuenta1 = CuentaBancaria("300929", ["ximena", "juan"], 1000000)
cuenta1.mostrar_detalles()

cuenta1.depositar(500000)
cuenta1.retirar(100000)
cuenta1.aplicar_cuota_manejo()

cuenta1.mostrar_detalles()
             
                                                                     