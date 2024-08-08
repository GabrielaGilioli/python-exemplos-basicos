# Solicita as alturas das duas pessoas
altura1 = float(input("Digite a altura da primeira pessoa (em metros): "))
altura2 = float(input("Digite a altura da segunda pessoa (em metros): "))

# Compara as alturas e exibe a mensagem apropriada
if altura1 > altura2:
    print(f"A primeira pessoa é mais alta, com {altura1} metros.")
elif altura2 > altura1:
    print(f"A segunda pessoa é mais alta, com {altura2} metros.")
else:
    print("As duas pessoas têm a mesma altura.")