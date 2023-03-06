# Lê os três números inteiros do usuário
num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota: "))
num3 = int(input("Digite a terceira nota: "))

# Calcula a média aritmética
media = (num1 + num2 + num3) / 3

# Verifica em qual faixa a média se encontra e exibe a mensagem correspondente
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
