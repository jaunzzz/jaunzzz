"""
Autor: João Manoel Naponucena Leite
Componente Curricular: EXA 854 - MI - Algoritimos
Concluído em: 
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
# Declaração das variáveis dos postos:
posto_1_nome = str(input("Informe o nome do seu posto: \n"))
valor_gasolina_posto_1 = float(input(f"Informe o valor da gasolina para {posto_1_nome}: \n"))
valor_etanol_posto_1 = float(input(f"Informe o valor do etanol para {posto_1_nome}: \n"))
valor_diesel_posto_1 = float(input(f"Informe o valor do disel para {posto_1_nome}: \n"))
print("\nSeu posto foi cadastrado com sucesso!\n")

posto_2_nome = str(input("Informe o nome do seu posto: \n"))
valor_gasolina_posto_2 = float(input(f"Informe o valor da gasolina para {posto_2_nome}: \n"))
valor_etanol_posto_2 = float(input(f"Informe o valor do etanol para {posto_2_nome}: \n"))
valor_diesel_posto_2 = float(input(f"Informe o valor do disel para {posto_2_nome}: \n"))
print("\nSeu posto foi cadastrado com sucesso!\n")

posto_3_nome = str(input("Informe o nome do seu posto: \n"))
valor_gasolina_posto_3 = float(input(f"Informe o valor da gasolina para {posto_3_nome}: \n"))
valor_etanol_posto_3 = float(input(f"Informe o valor do etanol para {posto_3_nome}: \n"))
valor_diesel_posto_3 = float(input(f"Informe o valor do disel para {posto_3_nome}: \n"))
print("\nSeu posto foi cadastrado com sucesso!\n")

# Declaração das variáveis do relatório:

consultas_realizadas = 0

vezes_posto_1_menor_valor = 0
vezes_posto_2_menor_valor = 0
vezes_posto_3_menor_valor = 0

litros_posto_1 = 0
litros_posto_2 = 0
litros_posto_3 = 0

# Loop do programa:
while True:
    print("""\n
Menu
1 - Realizar consulta de abastecimento;
2 - Listar todos os postos e suas informações;
3 - Sair (mostrar relatório);\n
""")
    opção = input("Escolha uma opção: ")

    if opção == "1":
        consultas_realizadas += 1
        combustivel = input("Informe o tipo de combustível (gasolina, etanol ou diesel): \n".lower())
        litros = float(input("Informe a quantidade de litros: \n"))

        menor_valor = float('inf')
        posto_menor_valor = ""

        valor_abastecimento_posto_1 = 0
        valor_abastecimento_posto_2 = 0
        valor_abastecimento_posto_3 = 0

        if combustivel == "gasolina":
            valor_abastecimento_posto_1 = valor_gasolina_posto_1 * litros
            valor_abastecimento_posto_2 = valor_gasolina_posto_2 * litros
            valor_abastecimento_posto_3 = valor_gasolina_posto_3 * litros

        elif combustivel == "etanol":
            valor_abastecimento_posto_1 = valor_etanol_posto_1 * litros
            valor_abastecimento_posto_2 = valor_etanol_posto_2 * litros
            valor_abastecimento_posto_3 = valor_etanol_posto_3 * litros
        elif combustivel == "diesel":
            valor_abastecimento_posto_1 = valor_diesel_posto_1 * litros
            valor_abastecimento_posto_2 = valor_diesel_posto_2 * litros
            valor_abastecimento_posto_3 = valor_diesel_posto_3 * litros
        else:
            print("Tipo de combustível inválido.")
            continue

        if valor_abastecimento_posto_1 < menor_valor:
            menor_valor = valor_abastecimento_posto_1
            posto_menor_valor = posto_1_nome
            litros_posto_1 += litros
            vezes_posto_1_menor_valor += 1

        if valor_abastecimento_posto_2 < menor_valor:
            menor_valor = valor_abastecimento_posto_2
            posto_menor_valor = posto_2_nome
            litros_posto_2 += litros
            vezes_posto_2_menor_valor += 1

        if valor_abastecimento_posto_3 < menor_valor:
            menor_valor = valor_abastecimento_posto_3
            posto_menor_valor = posto_3_nome
            litros_posto_3 += litros
            vezes_posto_3_menor_valor += 1

        print(f"""
Valor do abastecimento no {posto_1_nome}: R${valor_abastecimento_posto_1:.2f}
Valor do abastecimento no {posto_2_nome}: R${valor_abastecimento_posto_2:.2f}
Valor do abastecimento no {posto_3_nome}: R${valor_abastecimento_posto_3:.2f}
\nO posto com o menor valor para {combustivel} é {posto_menor_valor}.
""")

    elif opção == "2":
        print(f"""
\nLista de todos os postos e seus preços:\n
{posto_1_nome}: Gasolina - R${valor_gasolina_posto_1:.2f}, Etanol - R${valor_etanol_posto_1:.2f}, Diesel - R${valor_diesel_posto_1:.2f}
{posto_2_nome}: Gasolina - R${valor_gasolina_posto_2:.2f}, Etanol - R${valor_etanol_posto_2:.2f}, Diesel - R${valor_diesel_posto_2:.2f}
{posto_3_nome}: Gasolina - R${valor_gasolina_posto_3:.2f}, Etanol - R${valor_etanol_posto_3:.2f}, Diesel - R${valor_diesel_posto_3:.2f}
""")

    elif opção == "3":
        print(f"""
\n\tRelatório:
Quantidade de consultas realizadas: {consultas_realizadas}
Quantidade de vezes que os postos tiveram menor valor:
{posto_1_nome}: {vezes_posto_1_menor_valor}
{posto_2_nome}: {vezes_posto_2_menor_valor}
{posto_3_nome}: {vezes_posto_3_menor_valor}
""")
        break
    else:
        print("\nOpção inválida. Escolha uma opção válida.\n")
