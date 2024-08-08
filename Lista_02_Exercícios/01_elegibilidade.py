# Solicita o nome e a idade do usuário
nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))

# Verifica se a idade é suficiente para votar
if idade >= 16:
    print(f"{nome}, você tem {idade} anos e está apto(a) para votar.")
else:
    print(f"{nome}, você tem {idade} anos e ainda não está apto(a) para votar.")