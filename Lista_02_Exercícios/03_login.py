# Define as credenciais corretas
usuario_correto = "admin"
senha_correta = "1234"

# Solicita o nome de usuário e a senha do usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se o nome de usuário e a senha estão corretos
if usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido! Bem-vindo(a)!")
else:
    print("Erro: Nome de usuário ou senha incorretos.")