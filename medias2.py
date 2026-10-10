# função para calcular a média de duas notas e determinar se o aluno foi aprovado ou reprovado
def calcular_media(nota1, nota2, RA, aluno):
    #imprime na tela que as notas devem estar entre 0.0 e 10
    print("As notas devem estar entre 0.0 e 10")
    # solicita a primeira nota do usuário 
    nota1 = float(input("Digite a primeira nota: "))
    # valida se a nota está dentro do intervalo permitido
    while nota1 < 0 or nota1 > 10:
        # se nota1 for inválida, imprime mensagem
        print("Nota1 inválida. Digite uma nota entre 0.0 e 10")
        # solicita novamente a nota do usuário e valida se está dentro do intervalo permitido
        nota1 = float(input("Digite a primeira nota: "))
    # se nota1 for válida, imprime mensagem
    print("Nota1 válida.")

    # para a segunda nota, faz igual acima
    nota2 = float(input("Digite a segunda nota: "))   
    while nota2 < 0 or nota2 > 10:
        print("Nota2 inválida. Digite uma nota entre 0.0 e 10")
        nota2 = float(input("Digite a segunda nota: "))
    print("Nota2 válida.")

    # calcula a média das duas notas
    media = (nota1 + nota2) / 2
    return media
    # se media for maior ou igual a 6, imprime aprovado, caso contrário, imprime reprovado
    if media >= 6: 
        print(f"Desempenho: A media do aluno {aluno} RA: {RA} é: {media}. Aprovado")
    else:
        print(f"Desempenho: A media do aluno {aluno} RA: {RA} é: {media}. Reprovado")


# inicio do programa
print("Bem-vindo ao sistema de cálculo de médias da Escola Alpha.")


#variavel RA recebe o alfanumérico do registro acadêmico
RA = (input("Digite o Registro Acadêmico (RA): "))

#variavel aluno recebe o nome do aluno
aluno= (input("Digite o nome do aluno: "))

#print(f"RA: {RA} - Aluno: {aluno}")

#nota1 e nota2 são inicializadas com 0, mas serão sobrescritas pelos valores digitados pelo usuário
nota1 = 0
nota2 = 0

# Uso da função, função passa por parâmetro RA e aluno para a função acima
calcular_media(nota1, nota2, RA, aluno)


   