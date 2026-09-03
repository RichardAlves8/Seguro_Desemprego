#Variaveis Globais
temDireito, causa, salario_minimo = False, "Opção inválida", 1621.00 #Para validação 

#Serão usadas no final do algoritimo por isso eu às declarei aqui
beneficioSeguro_Recebidos = mesesTrabalhados = tipoBeneficio_Formal = duracaoDeCurso = 0

#Menu principal
print("Olá, seja bem vindo!")
print("Você está no menu de simulação do beneficio seguro-desemprego! Responda as perguntas abaixo para iniciar.")
print("De acordo com sua ultima atividade profissional, em quais dessas opções você se enquadra? \n")
print("1. Trabalhador Formal;")
print("2. Pescador Profissional Artesanal com Registro Ativo (Seguro-Defeso);")
print("3. Trabalhador Resgatado de regime de trabalho forçado (ou condição análoga à de escravo).")
criterioParaSeguro = int(input("(Digite 1, 2 ou 3) -> "))

if criterioParaSeguro == 1: #Trabalhador formal
    print("\nComo trabalhador formal, você foi:")
    print("1. Demitido(a) involuntariamente;")
    print("2. Suspenso(a) em virtude de participação de cursos ou programas de qualificação profissional.")
    tipoBeneficio_Formal = int(input(" -> ")) 
    estudante = (tipoBeneficio_Formal == 2)
    if tipoBeneficio_Formal <= 2 and tipoBeneficio_Formal > 0: #Sempre verdadeira mas evita que o usuário digite valor diferente  
        #só se a consulta for orientada à demissão (Situação 1) senão não há necessidade.
        formal_JustaCausa = ""
        if not estudante: formal_JustaCausa = input("O motivo da dispensa foi por justa causa? (S/N): ")

        if (formal_JustaCausa == "n" or formal_JustaCausa == "N") or estudante: 
                mesesTrabalhados = int(input("Quantos meses você trabalhou nesta empresa? : "))
                #Justa causa e trabalhado mais de 6 meses, mas ainda menos que 12, ou estudante   
                if mesesTrabalhados >= 6 :
                    if not estudante and mesesTrabalhados < 12:
                        primeiraEntrada = input("Já recebeu o benefio de seguro-desemprego alguma vez? (S/N): ")
                        if primeiraEntrada == "s" or primeiraEntrada == "S":
                            beneficioSeguro_Recebidos = int(input("Quantas vezes? : "))
                            if (beneficioSeguro_Recebidos == 1 and mesesTrabalhados >= 9) or (beneficioSeguro_Recebidos >= 2 and mesesTrabalhados >= 6):
                                #1º Entrada no mínimo de 12 (doze) meses; 
                                #2ª de 9 (nove) meses; 
                                #3ª ou mais no mínimo 6 (seis) meses.
                                temDireito=True
                            else: temDireito=False; causa=f"{mesesTrabalhados} meses trabalhados, para {beneficioSeguro_Recebidos + 1}ª benefícios já recebidos."
                    elif not estudante and mesesTrabalhados > 12:
                        temDireito = True
                    elif estudante: 
                            duracaoDeCurso = int(input("Quantos meses de duração tem o curso ou programa? : "))
                            if (duracaoDeCurso >= 2 and duracaoDeCurso <= 5):
                                temDireito = True
                            else:
                                temDireito = False; causa = f"{duracaoDeCurso} meses de curso" 
                else : temDireito=False; causa="menos de 6 meses de trabalho"  
        else: temDireito=False;causa="dispensa por justa causa."

elif criterioParaSeguro == 2: #Pescador Profissional
    #Fonte: https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/seguro-desemprego-do-pescador-artesanal
    print("\nComo Pescador Profissional Artesanal, você foi:\n")
    print("1. Impedido(a) de pescar, em função de período de defeso da espécie que captura;")
    print("2. Afastado(a) de sua função, deixou de comercializar a sua produção a pessoa física ou jurídica.")
    tipoBeneficio_Formal=int(input(" -> "))

    if tipoBeneficio_Formal <= 2 and tipoBeneficio_Formal > 0 : #hgn
        mesesTrabalhados = int(input(f"Por quantos meses exerceu a atividade de pesca antes de solicitar este benefício? : "))
        if mesesTrabalhados < 12:
            temDireito=False; causa="menos de 12 meses (1 ano) de pesca."
        else:temDireito=True

elif criterioParaSeguro == 3: #Seguro-Desemprego Trabalhador Resgatado
    print("\nO Seguro-Desemprego Trabalhador Resgatado é um auxílio temporário")
    print("Concedido ao trabalhador comprovadamente resgatado de  regime de trabalho forçado")
    print("A lei garante ao trabalhador o direito de receber o benefício por um período máximo de três meses.")
    temDireito = True

if not temDireito:
    if causa != "Opção inválida": print(f"De acordo com a simulação você não tem direito ao benefício, pois {causa} não se encaixam nos critérios para o Seguro-Desemprego. Para mais informações consulte o site Gov.br\n")
    else: print("Opção inválida! Encerrando...")
elif temDireito:
    #Variáveis de Cálculo
    ultimoMes = penultimoMes = antepenultimo = valor = 0.0
    numeroDeParcelas = 0
        
    #Questionário só sera requisitado se não for Trabalhador Resgatado
    if criterioParaSeguro < 3:    
        print("Você tem direito ao benefício de seguro-desemprego!")
        print("Para prosseguir com a simulação responda quais valor do seu sálario em seu:")
        ultimoMes = float(input("Último mês : "))
        penultimoMes = float(input("Penúltimo mês : "))
        antepenultimo = float(input("Antepenúltimo mês : "))

        #Cálculo: valor (https://www.calcule.net/trabalhista/calculo-seguro-desemprego/)
        media = (ultimoMes + penultimoMes + antepenultimo) / 3
        if media <= 2222.27: 
            valor = media * 0.80
        elif media >= 2222.28 and media <= 3703.99: 
            valor = (media * 0.5) + 1777.74  
        if valor > 3703.99: 
            valor = 2518.65 


        #Cálculo: número de numero De Parcelas (https://calculoexato.com.br/parprima.aspx?codMenu=TrabSegDesemprego)
        if not (criterioParaSeguro == 1 and tipoBeneficio_Formal == 2): #Exceto estudantes
            if (beneficioSeguro_Recebidos == 0 and (mesesTrabalhados >= 12 and mesesTrabalhados <= 23)): numeroDeParcelas = 4
            elif (beneficioSeguro_Recebidos == 0 and mesesTrabalhados >= 24): numeroDeParcelas = 5
            
            elif (beneficioSeguro_Recebidos == 1 and (mesesTrabalhados >= 9 and mesesTrabalhados <= 11)): numeroDeParcelas = 3
            elif (beneficioSeguro_Recebidos == 1 and (mesesTrabalhados >= 12 and mesesTrabalhados <= 23)): numeroDeParcelas = 4
            elif (beneficioSeguro_Recebidos == 1 and mesesTrabalhados >= 24): numeroDeParcelas = 5

            elif (beneficioSeguro_Recebidos >= 2 and (mesesTrabalhados >= 6 and mesesTrabalhados <= 11)): numeroDeParcelas = 3
            elif (beneficioSeguro_Recebidos >= 2 and (mesesTrabalhados >= 12 and mesesTrabalhados <= 23)): numeroDeParcelas = 4
            elif (beneficioSeguro_Recebidos >= 2 and mesesTrabalhados >= 24): numeroDeParcelas = 5
        else: #Bolsa Qualificação (https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/seguro-desemprego/bolsa-qualificacao)
            numeroDeParcelas = duracaoDeCurso
    else:
        numeroDeParcelas = 3 
        valor = 1621.00 #https://www.cartaoatacadao.com.br/blog/educacao-financeira/salario-minimo-o-que-e/#:~:text=O%20sal%C3%A1rio%20m%C3%ADnimo,oficial

    if valor < salario_minimo: valor = salario_minimo
    print(f"\nNumero de parcelas à receber: {numeroDeParcelas}\nValor: R${valor:.2f}\n")
