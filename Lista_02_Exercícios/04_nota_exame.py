# Solicita a nota do exame
nota = float(input("Digite a nota do exame: "))

# Usa o operador ternário para determinar se o aluno foi aprovado ou reprovado
mensagem = "Aprovado" if nota >= 5 else "Reprovado"

# Exibe a mensagem correspondente
print(mensagem)