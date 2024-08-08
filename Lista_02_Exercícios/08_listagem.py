# Define uma lista de nomes de alunos
alunos = ["luana", "kauê", "laura", "gabriela", "jhuan"]

# Exibe cada nome com um número sequencial usando um laço for
for indice, nome in enumerate(alunos, start=1):
    print(f"{indice}. {nome}")