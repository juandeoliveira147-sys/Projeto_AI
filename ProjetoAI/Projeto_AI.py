import random
import sys
import time
import json
import os


# aqui estaram algumas respostas aleatorias que seram usadas ao longo do codigo
respostas_de_erro = ["Errr essa alternativa está errada... tenta denovo, você consegue😊","Err você errou alguma coisa ao digitar😅...","Eu acho que você digitou algo errado... sem pressa...eu espero😊"]
tentativa_alta_demais = ["ixi, você tentou um numero muito alto, tenta um mais baixo😉","Não é esse numero😅 tenta um numero mais baixo","Você está tentando um numero alto demais....tenta um mais baixo😅"]
tentativa_baixa_demais = ["ixi, você tentou um numero muito baixo, tenta um mais alto😉","Não é esse numero😅 tenta um numero mais alto","Você está tentando um numero baixo demais....tenta um mais alto😅"]
acertou_o_numero = ["Parabéns, você acertouuu🎉🥳", "Incrivel, Você conseguiuuuuu🎉🥳", "Meus Parabéns, você conseguiu🎉"]

class coracao_da_AI():
    memoria = {}
    def carregar():
        if os.path.exists("memoria.json"):
            with open("memoria.json","r", encoding="utf-8")as arquivo:
                coracao_da_AI.memoria = json.load(arquivo)

            if "nome" in coracao_da_AI.memoria:
                return True
        return False

    def salvar():
        with open("memoria.json", "w", encoding="utf-8") as arquivo:
            json.dump(coracao_da_AI.memoria, arquivo, ensure_ascii=False, indent=4)

    def primeiro_acesso():
        print("Olá, me chamo AI, sua nova compania virtual😊")
        nome = input("Como eu poderia te chamar?🤗  ").strip().capitalize()
        print(f"Olá {nome}, é um prazer conhecer você")

        coracao_da_AI.memoria = {

            "nome": nome
        }

        coracao_da_AI.salvar()
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
                    return menu_da_AI.menu()
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
                print("\nVoltando para o menu do jogo...")
                time.sleep(3)
                return menu_da_AI.menu()
            
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
                        time.sleep(3)
                        return menu_da_AI.menu()

            elif numero_escolhido == 0:
                print("\nVocê digitou 0, o numero de saida")
                print("\nVoltando para o menu...")
                time.sleep(3)
                return menu_da_AI.menu()
                    


            
class menu_da_AI():
    
    def bem_vindo():
        nome = coracao_da_AI.memoria["nome"]
        print(f"\nOlá, bem vindo {nome}!😊")
        return menu_da_AI.menu()    
    def menu(): 
        nome = coracao_da_AI.memoria["nome"]
        print("\n============MENU==============")
        while True:
            escolha = input(f"O que gostaria de fazer agora {nome} ? 'calculadora', 'adivinhe o numero' ou 'sair': ").lower().strip()
            print("==============================\n")

            if escolha == 'sair':
                print(f"Até mais, {nome}! Te vejo na proxima👋😊.")
                time.sleep(3)
                sys.exit()


            elif escolha == 'calculadora':
                calculadora.menu_calculadora()

            elif escolha == 'adivinhe o numero':
                adivinhe_o_numero.menu_do_jogo()
                
            else:
                print("Opção inválida! Digite 'calculadora', 'adivinhe o numero' ou 'sair'.")
                continue

if __name__ == "__main__":

    if coracao_da_AI.carregar():
        menu_da_AI.bem_vindo()

    else:
        coracao_da_AI.primeiro_acesso()
        menu_da_AI.bem_vindo()
    
        