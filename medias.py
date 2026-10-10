def calcular_media(nota1, nota2): 
    print("As notas devem estar entre 0.0 e 10.0")
   
    nota1 = float(input("Digite a primeira nota: "))
    if nota1 >= 0 and nota1 <= 10:
        print("Nota1 válida.")
    else:
        print("Nota1 inválida. Digite uma nota entre 0.0 e 10.0")
        return None 
    nota2 = float(input("Digite a segunda nota: "))   
    if nota2 >= 0 and nota2 <= 10:
        print("Nota2 válida.")
    else:
        print("Nota2 inválida. Digite uma nota entre 0.0 e 10.0")  
        return None  
    media = (nota1 + nota2) / 2
    if media >= 6: 
        print(f"A media é: {media}. Aprovado")
    else:
        print(f"A media é: {media}. Reprovado")


# Dados de entrada (simulação)
print("Bem-vindo ao sistema de cálculo de médias da Escola Alpha.") 

nota1 = 0
nota2 = 0

# Uso das funções 
calcular_media(nota1, nota2)

# Saída do sistema 

   