def analisar_pontuacoes(pontuacoes):
    
    pontuacoes.sort(reverse=True)
    
    if pontuacoes[0] == pontuacoes[1] == pontuacoes[2]:
       return 'Nenhum clube subiu ou desceu'
    elif pontuacoes[0] == pontuacoes[1]:
        return f'o clube da {pontuacoes[2]} desceu para serie B.'
    else:
        return f'O clube da {pontuacoes[0]} subiu para a serie A.'


pontuacoes = []
for i in range(3):
    pontuacao = int(input(f'Digite a pontuação do clube {i+1}: '))
    pontuacoes.append(pontuacao)
    
resultado = analisar_pontuacoes(pontuacoes)
print(resultado)