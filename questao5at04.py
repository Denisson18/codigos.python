def trocar_roupa():
    resposta = input('Voce trocou de roupa? (s/n): ')
    return resposta.lower() == 's'
    
def tomar_banho():
    resposta = input('Voce trocou de roupa? (s/n): ')
    return resposta.lower() == 's'
    
def arrumar_quarto():
    resposta = input('Voce trocou de roupa? (s/n): ')
    return resposta.lower() == 's'
    
def fazer_janta():
    resposta = input('Voce trocou de roupa? (s/n): ')
    return resposta.lower() == 's'
    
def jantar():
    resposta = input('Voce trocou de roupa? (s/n): ')
    return resposta.lower() == 's'
    
def main():
    atividades = [trocar_roupa(), tomar_banho(), arrumar_quarto(), fazer_janta(), jantar()]
    
    if all(atividades):
        print('Voce fez todas as atividades. Hora de descansar!')
    else:
        print('Ainda há atividades pendentes')
if __name__ == '__main__':
    main()