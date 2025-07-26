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
        choices=["Atacar", "Ataque pesado"]
    ).ask()

    if escolha == "Atacar":
        acao_jogador = 1

    elif escolha == "Ataque pesado":
        acao_jogador = 2

    elif escolha == "Defender":
        acao_jogador = 3

def turno_inimigo():
    global acao_inimigo
    print("O inimigo esta pensando...")
    acao_inimigo = random.choice([3]) # 1 = Ataque, 2 = Ataque pesado, 3 = Defender
    time.sleep(1)

def comparar_acoes():
    global hp_inimigo, hp_jogador

    if acao_jogador in [1, 2]:
        if acao_inimigo == 3:
            chance = random.randint(0, 5)
            if chance == 5: #tentou defender mas falhou

                if acao_jogador == 1:
                    dano = random.choice([0, 5])
                elif acao_jogador == 2:
                    acerto = random.choice([0, 5])
                    if acerto == 5:
                        print("O Jogador errou o ataque!")
                        dano = 0.1
                    else:
                        dano = random.choice([3, 7]) 

                print("O inimigo tentou defender mas falhou!")
                time.sleep(1)
                hp_inimigo -= dano
                texto_grande(f"- {dano:.1f}", cor="bold red", fonte="standard")
                console.print(f"O jogador atacou e causou [bold red]{dano:.1f}[/bold red] de dano")

            else: #Conseguiu defender
                if chance == 1:
                    time.sleep(1)
                    console.print("O inimigo conseguiu defender completamente o ataque do jogador")
                else:
                    if acao_jogador == 1:
                        dano = random.choice([0, 5])
                    elif acao_jogador == 2:
                        acerto = random.choice([0, 5])
                        if acerto == 5:
                            print("O Jogador errou o ataque!")
                            dano = 0.1
                        else:
                            dano = random.choice([3, 7])

                    reducao = random.uniform(0.5, 2)
                    dano_final = dano - reducao
                    if dano_final < 0:
                        dano_final = 0  # evita dano negativo
                    hp_inimigo -= dano_final
                    texto_grande(f"- {dano_final:.1f}", cor="bold red", fonte="standard")
                    console.print(f"O Inimigo nao conseguiu defender mas reduziu o ataque do jogador em [bold red]{reducao:.1f}[/bold red]")
                    console.print(f"O Jogador causou um dano de [bold red]{dano_final:.1f}[/bold red]")




while True:
    barra_inimigo = "█" * int(hp_inimigo)
    barra_jogador = "█" * int(hp_jogador)
    console.print(f"HP JOGADOR: {barra_jogador} [bold green] {hp_jogador:.1f}[/bold green] --- HP INIMIGO: {barra_inimigo} [bold red]{hp_inimigo:.1f}[/bold red]")
    print("=-" * 45)
    turno_jogador()
    turno_inimigo()
    comparar_acoes()

    print(f"[ESCOLHAS] Inimigo = {acao_inimigo}, Jogador = {acao_jogador}")

    if hp_jogador <= 0:
        console.print("O jogador foi [bold red]DERROTADO![/bold red]")
        exit()
    elif hp_inimigo <= 0:
        console.print("O inimigo foi [bold red]DERROTADO![/bold red]")
        texto_grande(f"VITORIA", cor="bold green", fonte="standard")
        exit()
input()