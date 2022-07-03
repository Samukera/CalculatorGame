from models.calculator import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Nível de dificuldade [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Qual o resultado da operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos(s).')

    continuar: int = int(input('Deseja contnuar no jogo? [1 - sim, 0 - não] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).\nAté a próxima!')

if __name__ == '__main__':
    main()