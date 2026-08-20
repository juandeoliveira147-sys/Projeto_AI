from bancodedadosAI import conectar , encerrar_conexao
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import random
import sys
import time
import datetime





# aqui estaram algumas respostas aleatorias que seram usadas ao longo do codigo
respostas_de_erro = ["Errr essa alternativa está errada... tenta denovo, você consegue😊","Err você errou alguma coisa ao digitar😅...","Eu acho que você digitou algo errado... sem pressa...eu espero😊"]
tentativa_alta_demais = ["ixi, você tentou um numero muito alto, tenta um mais baixo😉","Não é esse numero😅 tenta um numero mais baixo","Você está tentando um numero alto demais....tenta um mais baixo😅"]
tentativa_baixa_demais = ["ixi, você tentou um numero muito baixo, tenta um mais alto😉","Não é esse numero😅 tenta um numero mais alto","Você está tentando um numero baixo demais....tenta um mais alto😅"]
acertou_o_numero = ["Parabéns, você acertouuu🎉🥳", "Incrivel, Você conseguiuuuuu🎉🥳", "Meus Parabéns, você conseguiu🎉"]

class coracao_da_AI():
    def carregar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS bancodedadosdaAI(
                        
                    nome varchar (100),
                    idade integer
                    );
                    """)
        conexao.commit()
        cursor.execute("SELECT * FROM bancodedadosdaAI")
        memoria = cursor.fetchall()
        cursor.close()
        encerrar_conexao(conexao)
        if memoria:
            menu_da_AI.bem_vindo(memoria)
        else:
           coracao_da_AI.primeiro_acesso()
        

            

    def primeiro_acesso():
        print("Olá, me chamo AI, sua nova compania virtual😊")
        nome = input("Como eu poderia te chamar?🤗  ").strip().capitalize()
        print(f"Olá {nome}, é um prazer conhecer você")
        while True:
            try:
                idade = int(input("\nQual a sua idade?: "))
            except ValueError:
                print("\nNão entendi sua idade")
                continue
            if idade > 1 :
                break
            else:
                print("\nAcho que sua idade está errada!")
                continue

        conec = conectar()
        cursor = conec.cursor()
        cursor.execute("""CREATE TABLE bancodedadosdaAI(

            nome varchar(100),
            idade integer,
            historico text,
            lembretes text
            );
            """)

        cursor.execute(f"INSERT INTO bancodedadosdaAI(nome , idade) values ('{nome}', '{idade}')")
        memoria = cursor.execute("SELECT * FROM bancodedadosdaAI")
        conec.commit()
        encerrar_conexao(conec)

        print(f"\né um prazer te conhecer {nome}")
        menu_da_AI.menu(memoria)

    def memoria():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("Select * from bancodedadosdaAI")
        memoria = cursor.fetchall()
        return memoria
    
    def lembretes():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("select lembretes from bancodedadosdaAI")
        memoria = cursor.fetchall()
        todos_lembretes = memoria[0][0]
        for linha in todos_lembretes.split('|'):
            lembrete = linha.strip().replace('[', "").replace(']','')
            if lembrete:
                print(lembrete)
        time.sleep(2)
        return
        



    def conversar():
        memoria = coracao_da_AI.memoria()
        nome = memoria[0][0]
        historico = memoria[0][2] if memoria[0][2] else ""  # Evita None
        lembretes = memoria[0][3] if memoria[0][3] else ""  # Puxa os lembretes atuais da única linha


        template = """
        Seu nome é AI. Você é a assistente Virtual do usuário. 
        Sua função é conversar e interagir sempre respondendo o usuário de uma forma dócil como se fosse uma amiga próxima mas também uma assistente.

        [CONTEXTO TEMPORAL]
        Hoje é dia: {data_atual}

        [LEMBRETES ATUAIS DO USUÁRIO]
        {lembretes}

        [DIRETRIZ DE LEMBRETES]
        Se o usuário pedir para adicionar, agendar ou salvar um lembrete (ex: "fazer dever de casa as 19h"):
        1. Você deve criar o novo lembrete calculando a data com base no dia de hoje ({data_atual}).
        2. Você DEVE incluir uma linha especial no FINAL da sua resposta escrita exatamente assim:
        REMANEJAR_LEMBRETES: [Aqui você repete TODOS os lembretes antigos exatamente como estão acima] | [Aqui você adiciona o novo lembrete]
        3. Se o usuário NÃO pedir nenhum lembrete, apenas converse normalmente e NÃO adicione a linha especial.

        [HISTÓRICO DA CONVERSA]
        {historico}

        [INFORMAÇÕES DO USUÁRIO]
        Nome: {nome}
        Gostos: Programação, anime, musica, curiosidades
        Objetivos: melhorar cada vez mais com programação e criar a AI 

        [PERGUNTA DO USUÁRIO]
        {pergunta}
        """


        model = OllamaLLM(model="llama3.1")
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model
        print("\nPara voltar ao menu digite 'sair'")
        while True:
            pergunta = input(f"\n{nome}: \n")
            
            if pergunta.strip().lower() == 'sair':
                print("\nVoltando para o menu...")
                time.sleep(2)
                break
                
            if not pergunta.strip():
                continue

            data_hoje = datetime.datetime.now().strftime("%d/%m/%Y (%A)")


            resultado = chain.invoke({
                "nome": nome,
                "data_atual": data_hoje,
                "historico": historico,
                "lembretes": lembretes,
                "pergunta": pergunta
            })


            if "REMANEJAR_LEMBRETES:" in resultado:

                partes = resultado.split("REMANEJAR_LEMBRETES:")
                resposta = partes[0].strip()
                novos_lembretes_acumulados = partes[1].strip()

                print(f"AI: {resposta}")
                

                lembretes = novos_lembretes_acumulados 
                
                try:
                    conexao = conectar()
                    cursor = conexao.cursor()
                    query_lembrete = "UPDATE bancodedadosdaAI SET lembretes = %s WHERE nome = %s;"
                    cursor.execute(query_lembrete, (lembretes, nome))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                except Exception as e:
                    print(f"Erro ao salvar lembrete: {e}")
            else:
                print(f"\nAI: {resultado}\n")
                resposta = resultado

            historico += f"\nUsuário: {pergunta}\nAI: {resposta}\n"

            try:
                conexao = conectar()
                cursor = conexao.cursor()
                query_historico = "UPDATE bancodedadosdaAI SET historico = %s WHERE nome = %s;"
                cursor.execute(query_historico, (historico, nome))
                conexao.commit()
                cursor.close()
                conexao.close()
            except Exception as e:
                print(f"Erro ao salvar histórico: {e}")
                
        return



    


        
class calculadora():
    def primeiro_numero():
        while True:
            try:
                num1 = int(input("Digite o primeiro numero: "))
                #poderia colocar o segundo numero aqui, mas quero que a pessoa possa escolher a operação antes do segundo numero
                return num1
            except ValueError:
                print("\nDigite um numero inteiro")
        

    

    def escolher_operacao():
        operacao = ("+","-","x","/","//","*","**","%")
        while True:
            qualoperacao = input("\nQual operação? ")
            if qualoperacao in operacao:
                break
            else:
                print("\nPor favor, Digite uma operação valida!")
                print("As operações são -, +, x, /, // , * , ** e  % \n")
        return qualoperacao
    
        
    def segundo_numero():
        while True:
            try:
                num2 = int(input("\nDigite o segundo numero: "))
                return num2
            except ValueError:
                print("\nDigite um numero inteiro: ")
        
    def divisor(num1,num2):
        try:
            resultado = num1 / num2
            return resultado 
        except ZeroDivisionError:
            return None
        
    

    def menu_calculadora():
        num1 =  calculadora.primeiro_numero()
        qualoperacao = calculadora.escolher_operacao()
        num2 = calculadora.segundo_numero()
        if qualoperacao == "+":
            resultado = num1 + num2
        elif qualoperacao == "-":
            resultado = num1 - num2
        elif qualoperacao in("x","*"):
            resultado = num1 * num2
        elif qualoperacao == "/":
            resultado = calculadora.divisor(num1 , num2)
        elif qualoperacao == "//":
            resultado = num1 // num2
        elif qualoperacao == "**":
            resultado = num1 ** num2
        elif qualoperacao == "%":
            resultado = num1 % num2

        if resultado is None:
            print("Não é possivel dividir por 0")
        else:
            print(f"\nO resultado de {num1}{qualoperacao}{num2} é {resultado}")

class adivinhe_o_numero():
    def menu_do_jogo():
        while True:
            saida = ("0")
            niveis = ("1","2","3")
            print("\nPara voltar para o menu, basta digitar 0 a qualquer momento,\n")
            print("\nEscolha o nivel de dificuldade:\n")
            print("1- de 1 a 100 numeros\n")
            print("2- de 1 a 1000 numeros\n")
            while True:
                escolha = input("3- de 1 a 10.000 nnumeros: selecione o nivel: ").strip().lower()
                if escolha in niveis:
                    break
                elif escolha in saida:
                    return
                else:
                    print("\nDigite o numero do nivel qude deseja jogar😊")
                    continue
            if escolha in niveis:
                if escolha in ("1"):
                    return adivinhe_o_numero.nivel(1)
                elif escolha in ("2"):
                    return adivinhe_o_numero.nivel(2)
                elif escolha in ("3"):
                    return adivinhe_o_numero.nivel(3)
            elif escolha in saida:
                print("\nVoltando para o menu ...")
                time.sleep(2)
                return
            
            else:
                print("\nVocê não escolheu um nivel correto")
                continue
    def nivel(nivel):
        if nivel == 1:
            print("\n==Bem vindo ao Nivel 1 do adivinhe o numero==\n")
            numero_secreto = random.randint(1,100)
            print("\n Seu numero secreto de 1 a 100 foi escolhido, vamos começar")
        elif nivel == 2:
            print("\n==Bem vindo ao Nivel 2 do adivinhe o numero==\n")
            numero_secreto = random.randint(1,1000)
            print("\n Seu numero secreto de 1 a 1000 foi escolhido, vamos começar")
        elif nivel == 3:
            print("\n==Bem vindo ao Nivel 3 do adivinhe o numero==\n")
            numero_secreto = random.randint(1,10000)
            print("\n Seu numero secreto de 1 a 10.000 foi escolhido, vamos começar")
        while True:
            try:
                numero_escolhido = int(input("\nDigite um numero: "))
            except ValueError:
                print("\n",random.choice(respostas_de_erro))
                continue

            if numero_escolhido != 0:
                if numero_escolhido > numero_secreto:
                    print("\n",random.choice(tentativa_alta_demais))
                    continue

                elif numero_escolhido < numero_secreto:
                    print("\n",random.choice(tentativa_baixa_demais))
                    continue

                elif numero_escolhido == numero_secreto:
                    print("\n",random.choice(acertou_o_numero))
                    print("\n1- jogar novamente")
                    escolha = input("2 - voltar para o menu: ").strip().lower()
                    if escolha in ("1","jogar novamente"):
                        return adivinhe_o_numero.menu_do_jogo()
                    elif escolha in ("2","voltar para o menu"):
                        print("\nVoltando para o menu...")
                        time.sleep(2)
                        return menu_da_AI.menu()

            elif numero_escolhido == 0:
                print("\nVocê digitou 0, o numero de saida")
                print("\nVoltando para o menu...")
                time.sleep(2)
                return menu_da_AI.menu()

                    
            
class menu_da_AI():
    
    def bem_vindo(memoria):
        nome = memoria[0][0]
        print(f"\nOlá, bem vindo {nome}!😊")
        menu_da_AI.menu(memoria)    
    def menu(memoria = None):
        if memoria is None:
            memoria = coracao_da_AI.memoria()
        nome = memoria[0][0]
        print("\n============MENU==============")
        while True:
            print(f"\nO que gostaria de fazer agora {nome} ?")
            print("\nCalculadora")
            print("Adivinhe o numero")
            print("Conversar")
            print("Lembretes")
            print("sair")
            escolha = input(f"resposta: ").lower().strip()
            print("==============================\n")

            if escolha == 'sair':
                print(f"Até mais, {nome}! Te vejo na proxima👋😊.")
                time.sleep(3)
                sys.exit()

            elif escolha in ("lembretes","lembrete"):
                coracao_da_AI.lembretes()

            elif escolha in ("conversar"):
                coracao_da_AI.conversar()
            elif escolha == 'calculadora':
                calculadora.menu_calculadora()

            elif escolha == 'adivinhe o numero':
                adivinhe_o_numero.menu_do_jogo()
                
            else:
                print("Opção inválida! Digite uma das opções")
                continue

if __name__ == "__main__":
    coracao_da_AI.carregar()
        
    
        