import random

def calcular_nivel(vitorias, derrotas):
    saldo_rankeadas = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_rankeadas, nivel

def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate! Ambos escolheram {}.".format(jogador1)
    elif (
        (jogador1 == "pedra" and jogador2 == "tesoura") or
        (jogador1 == "papel" and jogador2 == "pedra") or
        (jogador1 == "tesoura" and jogador2 == "papel")
    ):
        return "Jogador 1 vence! {} vence {}.".format(jogador1, jogador2)
    else:
        return "Jogador 2 vence! {} vence {}.".format(jogador2, jogador1)

print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")

vitorias_jogador1 = 0
derrotas_jogador1 = 0

for _ in range(3):

    escolhas_jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()


    while escolhas_jogador1 not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")
        escolhas_jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()

    escolhas_jogador2 = random.choice(["pedra", "papel", "tesoura"])


    resultado_rodada = jokenpo(escolhas_jogador1, escolhas_jogador2)


    print("Jogador 1 escolheu:", escolhas_jogador1)
    print("Jogador 2 escolheu:", escolhas_jogador2)

    print("Resultado:", resultado_rodada)

    if "Jogador 1 vence" in resultado_rodada:
        vitorias_jogador1 += 1
    else:
        derrotas_jogador1 += 1

saldo, nivel = calcular_nivel(vitorias_jogador1, derrotas_jogador1)

print(f"Saldo de Rankeadas Jogador 1: Vitórias = {vitorias_jogador1}, Derrotas = {derrotas_jogador1}")
print("Nível do jogador 1:", nivel)