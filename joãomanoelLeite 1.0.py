"""
Sistema operacional:  Windows 11
Versão Python: 3.11.4 64-bit
Autor: João Manoel Naponucena Leite
Componente Curricular: EXA 854 - MI - Algoritimos
Concluído em: 01/09/2023
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

# Declaração das variáveis relacionadas aos postos;
verificação_nome = False
while not verificação_nome:
    posto_1_nome = input("Informe o nome do posto: ")
    if posto_1_nome.strip(): 
        verificação_nome = True
    else:
        print("Você não digitou nada. Tente novamente.")

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor da gasolina para {posto_1_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_gasolina_posto_1 = float(valor_validação)

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor do etanol para {posto_1_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_etanol_posto_1 = float(valor_validação)

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor do diesel para {posto_1_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_diesel_posto_1 = float(valor_validação)

print("\nSeu posto foi cadastrado com sucesso!\n")

verificação_nome = False
while not verificação_nome:
    posto_2_nome = input("Informe o nome do posto: ")
    if posto_2_nome != posto_1_nome:
        if posto_2_nome.strip(): 
            verificação_nome = True
        else:
            print("Você não digitou nada. Tente novamente.")
    else:
        print("Já existe um posto com esse nome, tente outro.")

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor da gasolina para {posto_2_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_gasolina_posto_2 = float(valor_validação)

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor do etanol para {posto_2_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_etanol_posto_2 = float(valor_validação)

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor do diesel para {posto_2_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_diesel_posto_2 = float(valor_validação)

print("\nSeu posto foi cadastrado com sucesso!\n")

verificação_nome = False
while not verificação_nome:
    posto_3_nome = input("Informe o nome do posto: ")
    if posto_3_nome != posto_1_nome and posto_3_nome != posto_2_nome:
        if posto_3_nome.strip(): 
            verificação_nome = True
        else:
            print("Você não digitou nada. Tente novamente.")
    else:
        print("Já existe um posto com esse nome, tente outro.")    
        
validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor da gasolina para {posto_3_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_gasolina_posto_3 = float(valor_validação)

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor do etanol para {posto_3_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue
    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_etanol_posto_3 = float(valor_validação)

validação_entrada = False
while not validação_entrada:
    valor_validação = input(f"Informe o valor do diesel para {posto_3_nome}: \n")

    if not valor_validação:
        print("Nenhuma entrada fornecida! Tente novamente. \n")
        continue

    valor_validação = valor_validação.replace(',', '.')

    if valor_validação == '.' or valor_validação == ',':
        print("Entrada inválida! Tente novamente. \n")
        continue
    if valor_validação.count('-') >= 1:
        print("Entrada inválida! Tente novamente. \n")
        continue

    if '.' in valor_validação or ',' in valor_validação:
        if valor_validação.count('.') + valor_validação.count(',') > 1:
            print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
            continue

    if valor_validação == '0':
        print("Zero não é permitido! Tente novamente. \n")
    else:
        eh_numero = True
        for validação in valor_validação:
            if not (validação.isdigit() or validação == '.' or validação == '-'):
                eh_numero = False
                break
        if eh_numero:
            validação_entrada = True
        else:
            print("Entrada inválida! Tente novamente. \n")
valor_diesel_posto_3 = float(valor_validação)

print("\nSeu posto foi cadastrado com sucesso!\n")

# Declaração das variáveis do relatório;
consultas_realizadas = 0

vezes_posto_1_menor_valor = 0
vezes_posto_2_menor_valor = 0
vezes_posto_3_menor_valor = 0

litros_posto_1 = 0
litros_posto_2 = 0
litros_posto_3 = 0

nome_maior_preço_gasolina = ""
nome_maior_preço_etanol = ""
nome_maior_preço_diesel = ""
nome_menor_preço_gasolina = ""
nome_menor_preço_etanol = ""
nome_menor_preço_diesel = ""

# Menu;
print("""
=================== Menu =====================
1 - Realizar consulta de abastecimento;
2 - Listar todos os postos e suas informações;
3 - Sair (mostrar relatório);
==============================================
""")
opção = input("Escolha uma opção: \n")

# Loop principal do programa;
while opção != "3":
    # Opção 1;
    if opção == "1":
        consultas_realizadas += 1
        gasosa = False
        while not gasosa:
            combustivel = input("Informe o tipo de combustível (1-gasolina, 2-etanol ou 3-diesel): \n")
            if combustivel == "1":
                gasosa = True
            elif combustivel == "2":
                gasosa = True
            elif combustivel == "3":
                gasosa = True
            else:
                print("Tipo de combustível inválido.")
                
        validação_entrada = False
        while not validação_entrada:
            valor_validação = input("Informe a quantidade de litros: \n")
            if not valor_validação:
                print("Nenhuma entrada fornecida! Tente novamente. \n")
                continue
            valor_validação = valor_validação.replace(',', '.')
            if valor_validação == '.' or valor_validação == ',':
                print("Entrada inválida! Tente novamente. \n")
                continue
            if valor_validação.count('-') >= 1:
                print("Entrada inválida! Tente novamente. \n")
                continue
            if '.' in valor_validação or ',' in valor_validação:
                if valor_validação.count('.') + valor_validação.count(',') > 1:
                    print("Entrada inválida! Use apenas um ponto ou uma vírgula como separador decimal.")
                    continue
            if valor_validação == '0':
                print("Zero não é permitido! Tente novamente. \n")
            else:
                eh_numero = True
                for validação in valor_validação:
                    if not (validação.isdigit() or validação == '.' or validação == '-'):
                        eh_numero = False
                        break
                if eh_numero:
                    validação_entrada = True
                else:
                    print("Entrada inválida! Tente novamente. \n")
        litros = float(valor_validação)

        combustivel_nome = ""

        valor_abastecimento_posto_1 = 0
        valor_abastecimento_posto_2 = 0
        valor_abastecimento_posto_3 = 0
                
        calculo_de_economia_1 = 0
        calculo_de_economia_2 = 0

        if combustivel == "1":
            combustivel_nome = "gasolina"
            valor_abastecimento_posto_1 = valor_gasolina_posto_1 * litros
            valor_abastecimento_posto_2 = valor_gasolina_posto_2 * litros
            valor_abastecimento_posto_3 = valor_gasolina_posto_3 * litros
        elif combustivel == "2":
            combustivel_nome = "etanol"
            valor_abastecimento_posto_1 = valor_etanol_posto_1 * litros
            valor_abastecimento_posto_2 = valor_etanol_posto_2 * litros
            valor_abastecimento_posto_3 = valor_etanol_posto_3 * litros
        elif combustivel == "3":
            combustivel_nome = "diesel"
            valor_abastecimento_posto_1 = valor_diesel_posto_1 * litros
            valor_abastecimento_posto_2 = valor_diesel_posto_2 * litros
            valor_abastecimento_posto_3 = valor_diesel_posto_3 * litros

        if valor_abastecimento_posto_3 != valor_abastecimento_posto_1 != valor_abastecimento_posto_2 != valor_abastecimento_posto_3:
            if valor_abastecimento_posto_3 > valor_abastecimento_posto_1 < valor_abastecimento_posto_2:
                calculo_de_economia_1 = valor_abastecimento_posto_2 - valor_abastecimento_posto_1
                calculo_de_economia_2 = valor_abastecimento_posto_3 - valor_abastecimento_posto_1
                litros_posto_1 += litros
                vezes_posto_1_menor_valor += 1
                print(f"""\nO posto com o menor valor de abastecimento para {combustivel_nome} é o {posto_1_nome} custando: R${valor_abastecimento_posto_1:.2f}
Economia do {posto_1_nome} em relação aos demais:
{posto_2_nome}: R${calculo_de_economia_1:.2f}
{posto_3_nome}: R${calculo_de_economia_2:.2f}\n""")
            if valor_abastecimento_posto_1 > valor_abastecimento_posto_2 < valor_abastecimento_posto_3:
                calculo_de_economia_1 = valor_abastecimento_posto_1 - valor_abastecimento_posto_2
                calculo_de_economia_2 = valor_abastecimento_posto_3 - valor_abastecimento_posto_2
                litros_posto_2 += litros
                vezes_posto_2_menor_valor += 1
                print(f"""\nO posto com o menor valor de abastecimento para {combustivel_nome} é o {posto_2_nome} custando: R${valor_abastecimento_posto_2:.2f}
Economia do {posto_2_nome} em relação aos demais:
{posto_1_nome}: R${calculo_de_economia_1:.2f}
{posto_3_nome}: R${calculo_de_economia_2:.2f}\n""")
            if valor_abastecimento_posto_1 > valor_abastecimento_posto_3 < valor_abastecimento_posto_2:
                calculo_de_economia_1 = valor_abastecimento_posto_1 - valor_abastecimento_posto_3
                calculo_de_economia_2 = valor_abastecimento_posto_2 - valor_abastecimento_posto_3
                litros_posto_3 += litros
                vezes_posto_3_menor_valor += 1
                print(f"""\nO posto com o menor valor de abastecimento para {combustivel_nome} é o {posto_3_nome} custando: R${valor_abastecimento_posto_3:.2f}
Economia do {posto_3_nome} em relação aos demais:
{posto_1_nome}: R${calculo_de_economia_1:.2f}
{posto_2_nome}: R${calculo_de_economia_2:.2f}\n""")

        if valor_abastecimento_posto_1 == valor_abastecimento_posto_2 and valor_abastecimento_posto_1 < valor_abastecimento_posto_3 > valor_abastecimento_posto_2:
            calculo_de_economia_1 = valor_abastecimento_posto_3 - valor_abastecimento_posto_1
            litros_posto_1 += litros
            litros_posto_2 += litros
            vezes_posto_1_menor_valor += 1
            vezes_posto_2_menor_valor += 1
            print(f"""\nOs postos com o menor valor de abastecimento para {combustivel_nome} são: {posto_1_nome} e {posto_2_nome} custando ambos R${valor_abastecimento_posto_1:.2f}
Economia dos postos em relação ao {posto_3_nome}:
R${calculo_de_economia_1:.2f}""")

        if valor_abastecimento_posto_2 == valor_abastecimento_posto_3 and valor_abastecimento_posto_2 < valor_abastecimento_posto_1 > valor_abastecimento_posto_3:
            calculo_de_economia_1 = valor_abastecimento_posto_1 - valor_abastecimento_posto_3
            litros_posto_3 += litros
            litros_posto_2 += litros
            vezes_posto_3_menor_valor += 1
            vezes_posto_2_menor_valor += 1
            print(f"""\nOs postos com o menor valor de abastecimento para {combustivel_nome} são os: {posto_3_nome} e {posto_2_nome} custando ambos: R${valor_abastecimento_posto_3:.2f}
Economia dos postos em relação ao {posto_1_nome}:
R${calculo_de_economia_1:.2f}""")

        if valor_abastecimento_posto_1 == valor_abastecimento_posto_3 and valor_abastecimento_posto_1 < valor_abastecimento_posto_2 > valor_abastecimento_posto_3:
            calculo_de_economia_1 = valor_abastecimento_posto_2 - valor_abastecimento_posto_3
            litros_posto_1 += litros
            litros_posto_3 += litros
            vezes_posto_1_menor_valor += 1
            vezes_posto_3_menor_valor += 1
            print(f"""\nOs postos com o menor valor de abastecimento para {combustivel_nome} são os: {posto_1_nome} e {posto_3_nome} custando ambos: R${valor_abastecimento_posto_1:.2f}
Economia dos postos em relação ao {posto_2_nome}:
R${calculo_de_economia_1:.2f}""")
            
        if valor_abastecimento_posto_3 == valor_abastecimento_posto_1 == valor_abastecimento_posto_2 == valor_abastecimento_posto_3:
            litros_posto_1 += litros
            litros_posto_2 += litros
            litros_posto_3 += litros
            vezes_posto_1_menor_valor += 1
            vezes_posto_2_menor_valor += 1
            vezes_posto_3_menor_valor += 1
            print(f"""\nTodos os postos possuem o mesmo valor de abastecimento para {combustivel_nome}. custando: R${valor_abastecimento_posto_1:.2f}""")  
    # Opção 2;
    elif opção == "2":
        print(f"""Lista de todos os postos e seus preços:
=========================================================
{posto_1_nome}: Gasolina - R${valor_gasolina_posto_1:.2f} / Etanol - R${valor_etanol_posto_1:.2f} / Diesel - R${valor_diesel_posto_1:.2f}
{posto_2_nome}: Gasolina - R${valor_gasolina_posto_2:.2f} / Etanol - R${valor_etanol_posto_2:.2f} / Diesel - R${valor_diesel_posto_2:.2f}
{posto_3_nome}: Gasolina - R${valor_gasolina_posto_3:.2f} / Etanol - R${valor_etanol_posto_3:.2f} / Diesel - R${valor_diesel_posto_3:.2f}
=========================================================\n
""")
    else:
        print("\nOpção inválida. Escolha uma opção válida.\n")
    # Menu de repetição;
    print("""
=================== Menu =====================
1 - Realizar consulta de abastecimento;
2 - Listar todos os postos e suas informações;
3 - Sair (mostrar relatório);
==============================================
""")
    opção = input("Escolha uma opção: \n")

# Relatório após o fim da utilização;
print(f"""
=================== Relatório ========================
Quantidade de consultas realizadas: {consultas_realizadas}
Quantidade de vezes que os postos tiveram menor valor:
{posto_1_nome}: {vezes_posto_1_menor_valor}
{posto_2_nome}: {vezes_posto_2_menor_valor}
{posto_3_nome}: {vezes_posto_3_menor_valor}""")  
        
if vezes_posto_1_menor_valor == 0:
    litros_posto_1 = 0
    vezes_posto_1_menor_valor = 1
if vezes_posto_2_menor_valor == 0:
    litros_posto_2 = 0
    vezes_posto_2_menor_valor = 1
if vezes_posto_3_menor_valor == 0:
    litros_posto_3 = 0
    vezes_posto_3_menor_valor = 1

media_posto_1 = litros_posto_1 / vezes_posto_1_menor_valor
media_posto_2 = litros_posto_2 / vezes_posto_2_menor_valor
media_posto_3 = litros_posto_3 / vezes_posto_3_menor_valor

print(f"""Média de litros consultados por posto:
{posto_1_nome}: {media_posto_1:.2f}
{posto_2_nome}: {media_posto_2:.2f}
{posto_3_nome}: {media_posto_3:.2f}\n""")
        
maior_valor_gasolina = 0
menor_valor_gasolina = float("inf")

maior_valor_etanol = 0
menor_valor_etanol = float("inf")
        
maior_valor_diesel = 0
menor_valor_diesel = float("inf")
        
if valor_gasolina_posto_1 > maior_valor_gasolina:
    maior_valor_gasolina = valor_gasolina_posto_1
    nome_maior_preço_gasolina = posto_1_nome
if valor_gasolina_posto_2 > maior_valor_gasolina:
    maior_valor_gasolina = valor_gasolina_posto_2
    nome_maior_preço_gasolina = posto_2_nome
if valor_gasolina_posto_3 > maior_valor_gasolina:
    maior_valor_gasolina = valor_gasolina_posto_3
    nome_maior_preço_gasolina = posto_3_nome

if valor_etanol_posto_1 > maior_valor_etanol:
    maior_valor_etanol = valor_etanol_posto_1
    nome_maior_preço_etanol = posto_1_nome
if valor_etanol_posto_2 > maior_valor_etanol:
    maior_valor_etanol = valor_etanol_posto_2
    nome_maior_preço_etanol = posto_2_nome
if valor_etanol_posto_3 > maior_valor_etanol:
    maior_valor_etanol = valor_etanol_posto_3
    nome_maior_preço_etanol = posto_3_nome

if valor_diesel_posto_1 > maior_valor_diesel:
    maior_valor_diesel = valor_diesel_posto_1
    nome_maior_preço_diesel = posto_1_nome
if valor_diesel_posto_2 > maior_valor_diesel:
    maior_valor_diesel = valor_diesel_posto_2
    nome_maior_preço_diesel = posto_2_nome
if valor_diesel_posto_3 > maior_valor_diesel:
    maior_valor_diesel = valor_diesel_posto_3
    nome_maior_preço_diesel = posto_3_nome

if valor_gasolina_posto_1 < menor_valor_gasolina:
    menor_valor_gasolina = valor_gasolina_posto_1
    nome_menor_preço_gasolina = posto_1_nome
if valor_gasolina_posto_2 < menor_valor_gasolina:
    menor_valor_gasolina = valor_gasolina_posto_2
    nome_menor_preço_gasolina = posto_2_nome
if valor_gasolina_posto_3 < menor_valor_gasolina:
    menor_valor_gasolina = valor_gasolina_posto_3
    nome_menor_preço_gasolina = posto_3_nome
    menor_valor_etanol = valor_etanol_posto_1      
if valor_etanol_posto_1 < menor_valor_etanol:
    menor_valor_etanol = valor_etanol_posto_1
    nome_menor_preço_etanol = posto_1_nome
if valor_etanol_posto_2 < menor_valor_etanol:
    menor_valor_etanol = valor_etanol_posto_2
    nome_menor_preço_etanol = posto_2_nome
if valor_etanol_posto_3 < menor_valor_etanol:
    menor_valor_etanol = valor_etanol_posto_3
    nome_menor_preço_etanol = posto_3_nome

if valor_diesel_posto_1 < menor_valor_diesel:
    menor_valor_diesel = valor_diesel_posto_1
    nome_menor_preço_diesel = posto_1_nome
if valor_diesel_posto_2 < menor_valor_diesel:
    menor_valor_diesel = valor_diesel_posto_2
    nome_menor_preço_diesel = posto_2_nome
if valor_diesel_posto_3 < menor_valor_diesel:
    menor_valor_diesel = valor_diesel_posto_3
    nome_menor_preço_diesel = posto_3_nome
print(f"""Relação, por combustível, do posto que possui o maior valor e o menor valor:\n
Gasolina - Posto com o maior preço, menor preço e seu valor:
Maior preço: {nome_maior_preço_gasolina} - {maior_valor_gasolina:.2f} / Menor preço: {nome_menor_preço_gasolina} - {menor_valor_gasolina:.2f}\n
Etanol - Posto com o maior preço, menor preço e seu valor:
Maior preço: {nome_maior_preço_etanol} - {maior_valor_etanol:.2f} / Menor preço: {nome_menor_preço_etanol} - {menor_valor_etanol:.2f}\n
Diesel - Posto com o maior preço, menor preço e seu valor:
Maior preço: {nome_maior_preço_diesel} - {maior_valor_diesel:.2f} / Menor preço: {nome_menor_preço_diesel} - {menor_valor_diesel:.2f}\n""")
#Fim do progama;
