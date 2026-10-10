# Autor: Cristian Balsanelli
# Sistema de cálculo de médias - Escola Alpha

#variaveis recebem valores de notas
NOTA_MINIMA = 6.0
NOTA_MAXIMA = 10.0


# função que recebe e valida uma nota
def ler_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Digite a {numero_nota} nota: "))

            if 0 <= nota <= NOTA_MAXIMA:
                return nota

            print("Nota inválida! Digite um valor entre 0 e 10.")

        except ValueError:
            print("Entrada inválida! Digite um número válido.")


# funçaõ que Calcula a nota e devolve a média
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


# função que Determina a situação do aluno
def verificar_situacao(media):
    if media >= NOTA_MINIMA:
        return "Aprovado"
    else:
        return "Reprovado"


# Programa principal
#imprimre mensagem de boas-vindas
print("Bem-vindo ao sistema de médias da Escola Alpha.")

# Solicita RA e nome do aluno
RA = input("Digite o Registro Acadêmico (RA): ")
aluno = input("Digite o nome do aluno: ")

#recebem notas 1 e 2 e passam por parametro para a função calcular_media que valida se as notas estão entre 0 e 10
nota1 = ler_nota("primeira")
nota2 = ler_nota("segunda")

# passa por parametro as notas para a função calcular_media e recebe a média
media = calcular_media(nota1, nota2)

# passa por parametro a média para a função verificar_situacao e recebe a situação do aluno
situacao = verificar_situacao(media)

# imprime na tela relatorio final do aluno
print("\n--- RESULTADO DO ALUNO ---")
print(f"Aluno: {aluno}")
print(f"RA: {RA}")
print(f"Primeira nota: {nota1:.2f}")
print(f"Segunda nota: {nota2:.2f}")
print(f"Média final: {media:.2f}")
print(f"Situação: {situacao}")
