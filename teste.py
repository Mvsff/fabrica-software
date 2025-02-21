class Carro:
    def __init__(self, nome, modelo, marca):
        self.nome = nome
        self.modelo = modelo
        self.marca = marca
        self.em_movimento = False

    def andar(self):
        if not self.em_movimento:
            self.em_movimento = True
            print(f"{self.nome} ({self.marca} - {self.modelo}) está agora em movimento.")
        else:
            print(f"{self.nome} já está em movimento!")

    def estacionar(self):
        if self.em_movimento:
            self.em_movimento = False
            print(f"{self.nome} foi estacionado.")
        else:
            print(f"{self.nome} já está estacionado!")

# Criando instâncias de carros
carro1 = Carro("Fusca", "Sedan", "Volkswagen")
carro2 = Carro("Civic", "Sedan", "Honda")

# Testando os métodos
carro1.andar()
carro1.estacionar()

carro2.andar()
carro2.estacionar()
