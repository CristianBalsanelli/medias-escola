# 🎓 Sistema de Cálculo de Médias — Escola Alpha

![Sistema de Cálculo de Médias](sistema-medias.png)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Autor](https://img.shields.io/badge/Autor-Cristian%20Balsanelli-orange)

## 📚 Sobre o projeto

O **Sistema de Cálculo de Médias — Escola Alpha** é um programa desenvolvido em Python que recebe duas notas de um aluno, calcula a média final e informa se ele foi aprovado ou reprovado.

O projeto utiliza funções, estruturas de decisão, laços de repetição e tratamento de erros.

## 🎯 Funcionalidades

- 📝 Cadastro do nome e do Registro Acadêmico (RA).
- 🔢 Leitura e validação de duas notas entre 0 e 10.
- 🛡️ Tratamento de entradas inválidas.
- 🧮 Cálculo automático da média.
- ✅ Aprovação com média maior ou igual a 6,0.
- ❌ Reprovação com média inferior a 6,0.
- 📄 Exibição do relatório final do aluno.

## ⚙️ Como o programa funciona

### 1. Função `ler_nota()`

Recebe uma nota digitada pelo usuário e verifica se o valor está entre 0 e 10. Caso a entrada seja inválida, o programa solicita uma nova tentativa.

### 2. Função `calcular_media()`

Calcula a média aritmética das duas notas.

**Fórmula:**

`Média = (Nota 1 + Nota 2) / 2`

### 3. Função `verificar_situacao()`

Compara a média do aluno com a nota mínima de aprovação, definida pela constante `NOTA_MINIMA = 6.0`.

- ✅ Média maior ou igual a 6,0: Aprovado.
- ❌ Média inferior a 6,0: Reprovado.

## 💻 Exemplo de execução

```text
Bem-vindo ao sistema de médias da Escola Alpha.
Digite o Registro Acadêmico (RA): 123456
Digite o nome do aluno: João Silva
Digite a primeira nota: 8.5
Digite a segunda nota: 7.0

--- RESULTADO DO ALUNO ---
Aluno: João Silva
RA: 123456
Primeira nota: 8.50
Segunda nota: 7.00
Média final: 7.75
Situação: Aprovado
```

## 🧠 Conceitos de Python utilizados

| Conceito | Aplicação no projeto |
|---|---|
| Variáveis e constantes | Armazenamento de notas e limites |
| Funções | Organização e reutilização do código |
| `if` e `else` | Verificação da situação do aluno |
| `while` | Repetição até a entrada de uma nota válida |
| `try` e `except` | Tratamento de erros de conversão |
| `return` | Retorno dos resultados das funções |
| `f-strings` | Formatação das mensagens e do relatório |

## ▶️ Como executar

1. Instale o Python 3.
2. Salve o código em um arquivo chamado `sistema_medias.py`.
3. Abra o terminal na pasta do arquivo.
4. Execute o comando:

```bash
python sistema_medias.py
```

## 👨‍💻 Autor

**Cristian Balsanelli**

Projeto educacional desenvolvido para praticar lógica de programação, funções, validação de dados e estruturas de decisão em Python.

⭐ Se gostou do projeto, deixe uma estrela no repositório!


