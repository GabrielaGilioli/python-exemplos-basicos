# Exibe o menu de opções de comida
print("Menu de Opções de Comida:")
print("1: Pizza")
print("2: Hambúrguer")
print("3: Salada")

# Solicita ao usuário que escolha uma opção
opcao = int(input("Escolha uma opção (1, 2 ou 3): "))

# Usa a estrutura match para exibir a comida selecionada
match opcao:
    case 1:
        comida = "Pizza"
    case 2:
        comida = "Hambúrguer"
    case 3:
        comida = "Salada"
    case _:
        comida = "Opção inválida"

# Exibe a comida selecionada
print(f"Você escolheu: {comida}")