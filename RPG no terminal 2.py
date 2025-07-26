import random, questionary, time, pyfiglet
from rich.console import Console
console = Console()

hp_inimigo = 10
hp_jogador = 20
acao_jogador = 0
acao_inimigo = 0

def texto_grande(texto, cor="green", fonte="small"):
    ascii_art = pyfiglet.figlet_format(texto, font=fonte)
    console.print(ascii_art, style=cor)


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
    time.sleep(1)

def comparar_acoes():
    global hp_jogador, hp_inimigo, acao_jogador, acao_inimigo
    if acao_jogador == 1 and acao_inimigo == 2:
        acerto = random.randint(2, 5)
        if acerto == 5:
            acao_inimigo = 0
            ataque_jogador = random.randint(2, 7)
            hp_inimigo -= ataque_jogador
            print(f"O inimigo tentou defender mas falhou e o Jogador acertou um golpe de {ataque_jogador} de dano")
        else:
            print("O inimigo defendeu o ataque")
            time.sleep(0.5)
    elif acao_inimigo == 1 and acao_jogador == 2:
        acerto = random.randint(2, 5)
        if acerto == 5:
            acao_jogador = 0
            ataque_inimigo = random.randint(2, 7)
            hp_jogador -= ataque_inimigo
            texto_grande(f"- {ataque_inimigo}", cor="bold green", fonte="standard")
            print(f"O jogador tentou defender mas falhou, o Inimigo acertou um golpe de {ataque_inimigo} de dano")
        else:
            print("O Jogador defendeu o ataque")
            time.sleep(0.5)
    elif acao_jogador == 2 and acao_inimigo == 2:
        print("Mesmas escolhas, nada aconteceu")

    elif acao_jogador == 1 and acao_inimigo == 1:
        print("Ambos atacaram ao mesmo tempo!")
        ataque_jogador = random.choice([2, 4, 6, 8])
        ataque_inimigo = random.choice([2, 4, 6, 8])
        time.sleep(1.15)
        if ataque_jogador > ataque_inimigo:
            print(f"O jogador foi mais rapido e causou um dano de {ataque_jogador} no inimigo")
            time.sleep(1)
            print(f"O inimigo foi lento, causou um dano de apenas {ataque_inimigo / 2}")
            hp_jogador -= ataque_inimigo / 2
            hp_inimigo -= ataque_jogador
            texto_grande(f"- {ataque_inimigo / 2}", cor="bold green", fonte="standard")
        elif ataque_inimigo > ataque_jogador:
            print(f"O inimigo foi mais rapido e causou um dano de de {ataque_inimigo} no jogador")
            time.sleep(1)
            print(f"O jogador foi mais lento, causou um dano de apenas {ataque_jogador / 2}")
            hp_jogador -= ataque_inimigo
            hp_inimigo -= ataque_jogador / 2
            texto_grande(f"- {ataque_inimigo}", cor="bold green", fonte="standard")
        else:
            dano_empate = ataque_jogador / 2
            hp_inimigo -= dano_empate
            hp_jogador -= dano_empate
            texto_grande(f"- {dano_empate}", cor="bold green", fonte="standard")
            console.print(f"Ambos atacaram com a [bold bright_white]mesma forca![/bold bright_white]")
while True:
    barra_inimigo = "█" * int(hp_inimigo)
    console.print(f"HP JOGADOR:[bold red] {hp_jogador:.1f}[/bold red] --- HP INIMIGO: {barra_inimigo} [bold red]{hp_inimigo:.1f}[/bold red]")
    print("=-" * 45)
    turno_jogador()
    turno_inimigo()
    comparar_acoes()

    if hp_jogador <= 0:
        console.print("O jogador foi [bold red]DERROTADO![/bold red]")
        exit()
    elif hp_inimigo <= 0:
        console.print("O inimigo foi [bold red]DERROTADO![/bold red]")
        exit()