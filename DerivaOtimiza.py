from math import sqrt
def bhaskara(a, b, c):
    delta = (b * b) - (4 * a * c)
    if delta < 0:
        # Delta menor que 0, a função não tem raízes
        return None
    delta = sqrt(delta)
    r1 = (-b + delta) / (2 * a)
    r2 = (-b - delta) / (2 * a)
    return r1, r2

l = float(input("digite o lado do quadrado: "))


ptosCriticos=(bhaskara(12, -8*l, l**2))

ptoMaxima = ptosCriticos[0] if 24*ptosCriticos[0]-8*l < 0 else ptosCriticos[1]

volumeMaximo = 4*ptoMaxima**3-4*l*ptoMaxima**2+ptoMaxima*l**2
print("\n \n \n")

print("O maximo volume alcançado é: ", volumeMaximo ," unidades cubicas \n considerada a unidade usada para o lado")
print("A altura da 'parede' da caixa é : ", ptoMaxima)
