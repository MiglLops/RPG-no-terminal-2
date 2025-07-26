import random, rich, questionary, time

hp_inimigo = 10
hp_jogador = 20
acao_jogador = 0
acao_inimigo = 0

def turno_jogador():
    global acao_jogador
    escolha = questionary.select(
        "O que deseja fazer?",
        choices=["Atacar", "Defender"]
    ).ask()

    if escolha == "Atacar":
        acao_jogador = 1

    elif escolha == "Defender":
        acao_jogador = 2

def turno_inimigo():
    global acao_inimigo
    print("O inimigo esta pensando...")
    acao_inimigo = random.choice([1, 2]) # 1 = Ataque, 2 = Defesa
    time.sleep(0.84)
    print(f"Inimigo escolheu {acao_inimigo}")

def comparar_acoes():
    global hp_jogador, hp_inimigo, acao_jogador, acao_inimigo
    if acao_jogador == 1 and acao_inimigo == 2:
        acerto = random.randint(1, 5)
        if acerto == 5:
            acao_inimigo = 0
            ataque_jogador = random.randint(2, 7)
            hp_inimigo -= ataque_jogador
            print(f"O inimigo tentou defender mas falhou e o Jogador acertou um golpe de {ataque_jogador} de dano")
        else:
            print("O inimigo defendeu o ataque")
    
    elif acao_inimigo == 1 and acao_jogador == 2:
        acerto = random.randint(1, 5)
        if acerto == 5:
            acao_jogador = 0
            ataque_inimigo = random.randint(2, 7)
            hp_jogador -= ataque_inimigo
            print(f"O jogador tentou defender mas falhou, o Inimigo acertou um golpe de {ataque_inimigo} de dano")
        else:
            print("O Jogador defendeu o ataque")

    elif acao_jogador == 2 and acao_inimigo == 2:
        print("Mesmas escolhas, nada aconteceu")

    elif acao_jogador == 1 and acao_inimigo == 1:
        print("Ambos atacaram ao mesmo tempo!")
        ataque_jogador = random.choice([2, 4, 6, 8])
        ataque_inimigo = random.choice([2, 4, 6, 8])
        time.sleep(1.15)
        if ataque_jogador > ataque_inimigo:
            print(f"O jogador foi mais rapido e causou um dano de {ataque_jogador} no inimigo")
            print(f"O inimigo foi lento, causou um dano de apenas {ataque_inimigo / 2}")
            hp_jogador -= ataque_inimigo / 2
            hp_inimigo -= ataque_jogador
        elif ataque_inimigo > ataque_jogador:
            print(f"O inimigo foi mais rapido e causou um dano de de {ataque_inimigo} no jogador")
            print(f"O jogador foi mais lento, causou um dano de apenas {ataque_jogador / 2}")
            hp_jogador -= ataque_inimigo
            hp_inimigo -= ataque_jogador / 2
        else:
            print("WOW")

while True:
    turno_jogador()
    turno_inimigo()
    comparar_acoes()
    print(hp_inimigo, hp_jogador)
    if hp_jogador <= 0:
        print("O jogador foi derrotado!")
        exit()
    elif hp_inimigo <= 0:
        print("O inimigo foi derrotado!")
        exit()