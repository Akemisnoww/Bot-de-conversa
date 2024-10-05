def chatbot_responder(input_usuario):
    resposta = ""
    if 'olá' in input_usuario.lower() or 'oi' in input_usuario.lower():
        resposta = 'Olá! Como posso te ajudar hoje?'
    elif 'como você está?' in input_usuario.lower():
        resposta = 'Estou apenas um bot, mas estou em bom funcionamento! E você?'
    elif 'qual o seu nome amigo?' in input_usuario.lower():
        resposta = 'Meu nome é Cláudio, sou um robô simples, criado para te ajudar :)'
    elif 'adeus' in input_usuario.lower() or 'até logo' in input_usuario.lower():
        resposta = "Tchau! Foi um prazer conhecê-la(o)"
    else:
        resposta = 'Foi mal, não entendi, pode repetir por gentileza?'

    return resposta

def iniciar_chat():
    print('Cláudio: Olá! Eu sou seu amigo e assistente virtual.')
    while True:
        input_usuario = input('Você: ')

        if 'sair' in input_usuario.lower():
            print('Cláudio: Tchau! Até mais!')
            break

        resposta_bot = chatbot_responder(input_usuario)
        print('Cláudio:', resposta_bot)

iniciar_chat()