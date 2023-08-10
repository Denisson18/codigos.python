def validar_preço(produto_preço, limite_barato, limite_caro):
    if produto_preço <= limite_barato:
        return "barato"
    elif produto_preço >= limite_barato:
        return "caro"
    else:
        return "preço mais ou menos"
        
        
def main():
    limite_barato = 50
    limite_caro = 200

    try:
     produto_preço = float(input("digite o preço do produto"))
     resultado = validar_preço(produto_preço, limite_barato, limite_caro)
     print("O produto é:",resultado)
    
    except ValueError:
        print("Valor invalido. Veja se realmente voce digitou certo")
        
        
if __name__ == "__main__":
    main()