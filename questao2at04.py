def validar_estado(telefone):
    estados = {
        "82":'AL',
        '81':'PE',
        '71':'BA',
        '79':'SE',
        '85':'CE'
    }
    
    ddd = telefone[:2]
    
    if ddd in estados:
       return estados[ddd]
    else:
        return 'Nao achei o estado'
    
    numero_telefone = input('Digite o telefone com DDD. Tudo junto')
    
    estado = validar_estado(numero_telefone)
    
    print(f'O numero de telefone é do estado: (estado)')
    
if __name__ == '__main__':
    validar_estado
