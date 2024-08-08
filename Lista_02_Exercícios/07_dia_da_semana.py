# Solicita ao usuário que insira um dia da semana
dia_semana = input("Digite um dia da semana: ").strip().lower()

# Usa a estrutura match para verificar se é dia útil ou fim de semana
match dia_semana:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        tipo_dia = "Dia útil"
    case "sábado" | "sabado" | "domingo":
        tipo_dia = "Fim de semana"
    case _:
        tipo_dia = "Dia inválido"

# Exibe o resultado
print(f"{dia_semana.capitalize()} é {tipo_dia}.")