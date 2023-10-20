class Heroi:
    def __init__(self):
        self.experiencia = 0

    def atacar(self, inimigo):
        print("Inimigo apareceu")
        atacar = input("Deseja atacar o inimigo? (S/N) ")

        if atacar.upper() == 'S':
            print("Você atacou o inimigo")
            # Suponha que o herói causa 20 de dano ao inimigo
            dano_causado = 100
            inimigo.sofrer_dano(dano_causado)

            if inimigo.vida <= 0:
                self.ganhar_experiencia(inimigo.xp_dropado)
                print("Inimigo derrotado! Ganhou", inimigo.xp_dropado, "de experiência.")
                return True  # Retorna True se o inimigo foi derrotado
        else:
            print("Você optou por não atacar. Infelizmente, o inimigo te derrotou.")
            print("Você dropou 0 de experiência.")
            return False  # Retorna False se o jogador optou por não atacar
                  

    def ganhar_experiencia(self, xp_ganho):     
        self.experiencia += xp_ganho
        
    def exibir_classificacao(self):
      classificacao = self.obter_classificacao()
      print("Classificação do herói:", classificacao)

    def obter_classificacao(self):
        if self.experiencia < 1000:
            return "Ferro"
        elif 1001 <= self.experiencia <= 2000:
            return "Bronze"
        elif 2001 <= self.experiencia <= 5000:
            return "Prata"
        elif 6001 <= self.experiencia <= 7000:
            return "Ouro"
        elif 7001 <= self.experiencia <= 8000:
            return "Platina"
        elif 8001 <= self.experiencia <= 9000:
            return "Ascendente"
        elif 9001 <= self.experiencia <= 10000:
            return "Imortal"
        else:
            return "Radiante"


class Inimigo:
    def __init__(self):
        self.vida = 100
        self.xp_dropado = 950

    def sofrer_dano(self, dano):
        self.vida -= dano

if __name__ == "__main__":
    # Criando um herói
    heroi = Heroi()

    while True:  # Loop principal
        # Criando um novo inimigo
        inimigo_atual = Inimigo()

        # O herói ataca o inimigo
        derrotou_inimigo = heroi.atacar(inimigo_atual)

        # Exibindo a quantidade de xp dropada pelo inimigo, a vida restante do inimigo e a experiência do herói
        if derrotou_inimigo:
            print("XP dropado pelo inimigo:", inimigo_atual.xp_dropado)
            print("Experiência do herói:", heroi.experiencia)
            heroi.exibir_classificacao()
        else:
            break  # Sai do loop se o jogador optou por não atacar