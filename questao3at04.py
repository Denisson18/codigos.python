def analisar_glicose(taxas):
    media = sum(taxas) / len(taxas)
    
    if media > 6:
        return 'DIABETICO'
    else:
        return 'PRÉ-DIABETICO'
        
#loop finito de 4 voltas
taxas = []
for i in range(3):
    taxa = float(input(f'Digite a taxa de glicose do mês {i+1}: '))
    taxas.append(taxas)
    
    
resultado = analisar_glicose(taxas)
print(f'O paciente está  {resultado}. ')