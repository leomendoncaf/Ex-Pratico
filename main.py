# Convencional

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

# Factory

def criar_circulo(raio):
    def calcular_area():
        return 3.14 * raio ** 2

    return {
        'raio': raio,
        'calcular_area': calcular_area
    }

# Usando a classe/função convencional
circulo1 = Circulo(5)
area1 = circulo1.calcular_area()
print(area1)  # Saída: 78.5

# Usando a factory
circulo2 = criar_circulo(5)
area2 = circulo2['calcular_area']()
print(area2)  # Saída: 78.5
