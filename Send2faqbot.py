import telepot
import random
import time
import faq

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    uid = msg['from']['username']
    print('Got command {} '.format(command))
     
	#Hello World
    if command == '/ajuda':
        bot.sendMessage(chat_id, 'Olá {}, eu sou seu assistente pessoal aqui na plataforma. Eu posso te ajudar com dúvidas simples porém nada tão complexo. Meus desenvolvedores ainda estão trabalhando em meu cérebro, no momento ele ainda não é lá grande coisa, mas posso ajudar ou pelo menos tentar. Se você não ficar satisfeito com a minha ajuda você pode sempre buscar ajuda pelo Email atendimento@bitcambio.com.br, pelo live chat no site ou pelo Facebook. Sempre que você quiser saber algo, comece com / e depois digite a dúvida, por exemplo, caso queira saber como fazer um depósito, digite a / e depois digite: deposito em reais e então eu vou responder.'.format(uid))
    elif command == '/depositos':
        bot.sendMessage(chat_id, '{} veja esse material em nosso faq para dúvidas relacionadas com depósitos em reais e bitcoins:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003222167-Dep%C3%B3sitos'.format(uid))

    elif command == '/conta':
        bot.sendMessage(chat_id, 'Oi {} para dúvidas relacionadas com criação ou validação de conta, por favor, siga esse link para ver nosso faq:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003222147-Cadastro'.format(uid))

    elif command == '/saques':
        bot.sendMessage(chat_id, '{} veja em nosso faq as principais dúvidas relacionadas com o saque e como resolver:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003218228-Saques'.format(uid))

    elif command == '/boletos':
        bot.sendMessage(chat_id, '{} temos um tutorial para pagamento de boletos aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003220348-Servi%C3%A7oss'.format(uid))

    elif command == '/envio de dinheiro':
        bot.sendMessage(chat_id, '{} se você seguir esse link você encontra um tutorial para envio de dinheiro:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003220348-Servi%C3%A7os'.format(uid))

    elif command == '/comprar':
        bot.sendMessage(chat_id, '{} tudo bem? Veja como comprar ou vender aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003220428-Compra-Vendas'.format(uid))

    elif command == '/vender':
        bot.sendMessage(chat_id, '{} tudo bem? Veja como comprar ou vender aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003220428-Compra-Vendas'.format(uid))

    elif command == '/segurança':
        bot.sendMessage(chat_id, '{} temos ótimos tutoriais sobre segurança aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003220588-Seguran%C3%A7a'.format(uid))
	    
    elif command == '/conta':
        bot.sendMessage(chat_id, '{} Se você está tendo qualquer tipo de problemas com a sua conta, por favor, siga esse link:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003219988-Conta'.format(uid))
    
    elif command == '/login':
        bot.sendMessage(chat_id, '{} Caso tenha perdido a senha ou não consiga logar, siga esse link:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003295348-Login'.format(uid))

    elif command == '/problema com saques':
        bot.sendMessage(chat_id, '{} eu acho que esse link pode te ajudar a resolver os problemas com saque:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003224167-Saques'.format(uid))
	
    elif command == '/envio de dinheiro':
        bot.sendMessage(chat_id, '{} talvez esse link te ajude a resolver os problemas com envio de dinheiro:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003224187-Envio-de-dinheiro'.format(uid))
	
    elif command == '/validação de conta':
        bot.sendMessage(chat_id, '{} aqui, esse link te leva até os principais problemas relacionados com validação de conta:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003219948-Valida%C3%A7%C3%A3o-de-conta'.format(uid))
	
    elif command == '/login':
        bot.sendMessage(chat_id, '{} Caso tenha perdido a senha ou não consiga logar, siga esse link:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003295348-Login'.format(uid))

    elif command == '/depositos':
        bot.sendMessage(chat_id, '{} Caso tenha perdido a senha ou não consiga logar, siga esse link:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003219928-Dep%C3%B3sitos'.format(uid))

    elif command == '/problema com boletos':
        bot.sendMessage(chat_id, '{} Seu problema com boletos pode ser resolvido seguindo esse link:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003295348-Login'.format(uid))

    elif command == '/comunicação':
        bot.sendMessage(chat_id, '{} Ok, sem problemas, segue um link para te ajudar:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003224727-Comunica%C3%A7%C3%A3o'.format(uid))

    elif command == '/outros':
        bot.sendMessage(chat_id, '{} esse link pode te ajudar:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003438187-Outros'.format(uid))

    elif command == '/login':
        bot.sendMessage(chat_id, '{} Caso tenha perdido a senha ou não consiga logar, siga esse link:  https://bitcambiohelp.zendesk.com/hc/pt-br/sections/115003295348-Login'.format(uid))
		
    elif command == '/limites':
        bot.sendMessage(chat_id, '{} você pode ver todos os limites aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/categories/115001851288-Limites'.format(uid))

    elif command == '/prazos':
        bot.sendMessage(chat_id, '{} todos os nossos prazos você encontra aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/categories/115001846368-Prazos'.format(uid))

    elif command == '/taxas':
        bot.sendMessage(chat_id, '{} veja todas as nossas taxas aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/categories/115001845548-Taxas'.format(uid))

    elif command == '/bitcoin':
        bot.sendMessage(chat_id, '{} tudo bem com você? Nós temos um incrível material sobre bitcoins aqui:  https://bitcambiohelp.zendesk.com/hc/pt-br/categories/115001852227-Bitcoin'.format(uid))
 
	
	
bot = telepot.Bot('BOTFATHERTOKEN')
bot.message_loop(handle)

print('Working...')
while 1:
    time.sleep(10)

