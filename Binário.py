#============================ CONVERSOR BINÁRIO =============================
print('+-------------------+\n| Conversor Binário |\n+-------------------+') # Print de um pequeno título.
#================================ Input numero ==============================
binario = ' ' # Definiu variável "binario" como uma string vazia.
digito = int(input('>>> Número para a conversao: ')) # Input para o usuario digitar o numero para a conversão.
#========================= Converte binário =================================
while digito > 0: # Estrutura de repeticao que sera executada em quanto digito for maior que 0.
    resto = digito % 2 # Variável "resto" armazenando resto da divisao do digito.
    if resto == 1: #Estrutura que compara se o resto é igual a 1.
        binario= '1' + binario #Acumula o digito 1 na variavel binario.
        digito = digito//2 #Faz uma divisao inteira do digito.
    else: # E de o resto eh igual a 0.
        binario = '0' + binario # Acumula o digito 0 na variavel binario.
        digito = digito // 2 # Faz uma divisao inteira do digito.
#========================== Print Resultado =================================
print('>>> Número Convertido:',binario) # Printa o numero convertido em binario.
