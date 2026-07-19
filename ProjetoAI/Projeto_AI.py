import random

print("Olá, me chamo AI, sua nova compania virtual😊")
nome = input("Como eu poderia te chamar?🤗  ").strip()
print(f"Olá {nome}, é um prazer conhecer você")

# Loop principal para o menu nunca fechar sozinho
while True:
    print("\n==============================")
    escolha = input(f"O que gostaria de fazer agora {nome}? 'calculadora', 'adivinhe o numero' ou 'sair': ").lower().strip()
    print("==============================\n")

    if escolha == 'sair':
        print(f"Até mais, {nome}! Te vejo na proxima👋😊.")
        break

    # --- MENU DA CALCULADORA ---
    elif escolha == 'calculadora':
        print("Vamos começar, abrindo calculadora!")
        print("=== CALCULADORA INFINITA ===")
        print("Para voltar ao menu principal, digite 'sair' a qualquer momento.\n")
        
        while True:
            # 1. Entrada do primeiro número
            entrada1 = input("Digite o primeiro número: ")
            if entrada1.lower().strip() == 'sair':
                break
                
            # 2. Entrada da operação
            operacao = input("Digite a operação (+, -, *, /): ")
            if operacao.lower().strip() == 'sair':
                break
                
            # 3. Entrada do segundo número
            entrada2 = input("Digite o segundo número: ")
            if entrada2.lower().strip() == 'sair':
                break

            # Proteção contra letras ou caracteres inválidos nos números
            try:
                num1 = float(entrada1)
                num2 = float(entrada2)
            except ValueError:
                print("-> Erro: Você digitou uma letra! Use apenas números.\n")
                continue

            # 4. Processamento matemático
            if operacao == "+":
                resultado = num1 + num2
                print(f"-> Resultado: {num1} + {num2} = {resultado}\n")
                
            elif operacao == "-":
                resultado = num1 - num2
                print(f"-> Resultado: {num1} - {num2} = {resultado}\n")
                
            elif operacao == "*":
                resultado = num1 * num2
                print(f"-> Resultado: {num1} * {num2} = {resultado}\n")
                
            elif operacao == "/":
                if num1 == 0 and num2 == 0:
                    print("-> Resultado: Indefinido! Zero dividido por zero não existe.\n")
                elif num2 == 0:
                    print("-> Erro: Não é possível dividir por zero.\n")
                else:
                    resultado = num1 / num2
                    print(f"-> Resultado: {num1} / {num2} = {resultado}\n")
            else:
                print("-> Operação inválida! Tente novamente.\n")

    # --- MENU DO JOGO ---
    elif escolha == 'adivinhe o numero':
        print("Vamos começar, irei escolher o número e você irá chutá-lo.")
        print("Para desistir e voltar ao menu, digite '0'.\n")
        
        numero_secreto = random.randint(1, 100)
        
        while True:
            entrada_chute = input("Chute um número entre 1 e 100: ")
            
            # Proteção caso digitem letras no jogo
            try:
                chute = int(entrada_chute)
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
                continue

            if chute == 0:
                print("Saindo do jogo...")
                break
            elif chute > numero_secreto:
                print("Muito alto! Tenta mais uma vez.")
            elif chute < numero_secreto:
                print("Muito baixo! Tente novamente.\n")
            else:
                print(f"Acertou🥳🎊, você conseguiu! Meus Parabéns, {nome}!\n")
                print("Quando quiser aumentar o nível escreva 'nivel2' ")
                break # Venceu o jogo, volta para o menu principal




    elif escolha == 'nivel2':
        print("Vamos começar o Nivel 2, irei escolher o número e você irá chutá-lo.")
        print("Para desistir e voltar ao menu, digite '0'.\n")
        
        numero_secreto = random.randint(1, 1000)
        
        while True:
            entrada_chute = input("Chute um número entre 1 e 1000: ")
            
            # Proteção caso digitem letras no jogo
            try:
                chute = int(entrada_chute)
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
                continue

            if chute == 0:
                print("Saindo do jogo...")
                break
            elif chute > numero_secreto:
                print("Muito alto! Tenta mais uma vez.")
            elif chute < numero_secreto:
                print("Muito baixo! Tente novamente.\n")
            else:
                print(f"Acertou🥳🎊, você conseguiu! Meus Parabéns, {nome}!\n")
                break # Venceu o jogo, volta para o menu principal
    else:
        print("Opção inválida! Digite 'calculadora', 'adivinhe o numero' ou 'sair'.")