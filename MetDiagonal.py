posiçao = int(input("Digite um posição: "))

diagonal = 1
cont = 1

while True:
    for numerador in range(1, diagonal + 1):
        denominador = diagonal - numerador + 1

        if cont == posiçao:
            resultado = f"{numerador} / {denominador}"
            break

        cont += 1
    
    if cont == posiçao:
        break

    diagonal += 1

print(f"O número racional na posição {posiçao} é ->>> {resultado}")
