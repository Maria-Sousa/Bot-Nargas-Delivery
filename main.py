import requests
import time
import json


class TelegramBot:
  def __init__(self):
    token = '5630419846:AAGtpLVnMjmvRGzoIQTGEHkaa_m9-UxbpZ0'
    self.url_base = f'https://api.telegram.org/bot{token}/'
  #Iniciar o bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          eh_primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem,eh_primeira_mensagem)
          self.responder(resposta, chat_id)
  #Obter Mensagens
  def obter_mensagens(self,update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)
  #criar uma resposta
  def criar_resposta(self,mensagem,eh_primeira_mensagem):
    mensagem= mensagem['message']['text']
    if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
      return f'''Olá Bem vindo a Nargas Delivery, digite o que deseja:
      1-Essência 
      2- Carvão 
      3-Aluminio'''
    if mensagem =='1':
      return f'''
      4- Zomo R$8,00
      5- Onix R$12,00 
      6- Ziggy 12,00'''
    if mensagem == '4':
        return f'''confirmar pedido(s/n)'''
    if mensagem == '5':
        return f'''confirmar pedido(s/n)'''
    if mensagem == '6':
        return f'''confirmar pedido(s/n)'''
    if mensagem == '2':
      return f'''Papel Aluminio R$15,00
      Confirmar pedido(s/n)'''
    if mensagem =='3':
      return f'''Caixa carvão 12 unidades R$15,00
      confirmar pedido(s/n)'''

    if mensagem.lower() in ('s', 'sim'):
      return 'Pedido Confirmado!'
    else:
      return'Gostaria de acessar o menu? Digite "menu"'
    
  def responder(self, resposta, chat_id):
    #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()

