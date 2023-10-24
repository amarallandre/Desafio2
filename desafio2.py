class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque indefinido"

        mensagem = f"O {self.tipo} atacou, usou {ataque}."
        print(mensagem)

# Questionário para criar o personagem
nome = input("Qual é o nome do seu herói? ")
idade = int(input("Qual é a idade do seu herói? "))
print("Escolha o tipo do seu herói:")
print("1. Guerreiro")
print("2. Mago")
print("3. Monge")
print("4. Ninja")

opcao_tipo = input("Digite o número correspondente ao tipo do seu herói: ")

# Mapeia a opção escolhida para o tipo de herói
opcoes_tipo = {"1": "guerreiro", "2": "mago", "3": "monge", "4": "ninja"}
tipo_escolhido = opcoes_tipo.get(opcao_tipo, "indefinido")

# Cria o herói com base nas respostas do questionário
heroi = Heroi(nome=nome, idade=idade, tipo=tipo_escolhido)

print("Um dragão apareceu!")

# Agora, o herói está pronto para atacar
tipo_ataque_usuario = input("Deseja atacar o inimigo? S/N: ")
if tipo_ataque_usuario.upper() == "S":
    heroi.atacar()
else:
    print("Você morreu!")