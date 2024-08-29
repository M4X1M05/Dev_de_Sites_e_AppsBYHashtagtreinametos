# Titulo: Bolt assitente
# botão: iniciar chat
#popup/modal/alerta
# titulo: bem vindo ao Bolt seu assistente domiciliar
# campo de texto: escreva seu nome no chat
# botão: entrar no chat 
# sumir com o titulo e o botão inicial
# fechar o popup
#criar o chat ( com mensagem de "nome do usuario entrou no chat")
#embaixo do chat
#campo de texto : digite sua mensagem
#Botão enviar
#vai aparecer a mensagem no chat com o nome do usuário
#lira : coe galera
#  importar o flet
import flet as ft
 # criar a função principal do seu sistema
def main(pagina):
    # criar alguma coisa
    # criar o titulo 
    titulo = ft.Text("Bolt assistente")
    def enviar_mensagem_tunnel(mensagem):
     chat.controls.append(ft.Text(mensagem))
     pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunnel) # cria o tunel de comunicação   
    titulo_janela = ft.Text("Bem vindo ao Bolt assistente")
    campo_nome_usuario = ft.TextField(label="escreva a sua solicitação no chat")
    texto_mensagem = ft.TextField(label="Digite o seu problema/duvida")
        
   
    
    
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
       
        # enviar a mensagem no chat
            # Usuario: mensagem
   
    
        
        
        #enviar uma mensagem no tunnel
    pagina.pubsub.send_all("cliente entrou no chat") # envia uma mensagem no tunel
          # limpar o campo de mensagem
    texto_mensagem.value = ""
    pagina.update()
        
      
      
  
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    chat = ft.Column()
    
    # colunas e linhas
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])
    
    
    def entrar_chat(evento):
      
      # tirar o titulo da pagina
      pagina.remove(titulo)
    
      # tirar o botao_iniciar
      pagina.remove(botao_iniciar)
    
      # fechar o popup/janela
      janela.open = False
      # criar chat
      pagina.add(chat)
      # adicionar a linha de mensagem
      
      pagina.add(linha_mensagem)
      
      # escrever a mensagem: usuario entrou no chat
      texto_entrou_chat = f"{campo_nome_usuario} o cliente entrou no chat"
      chat.controls.append(ft.Text(texto_entrou_chat))
      pagina.update()
    
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
      
    janela = ft.AlertDialog(
    title=titulo_janela,
    content=campo_nome_usuario,
    actions=[botao_entrar]
      )
    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        print("Clicou no botão")
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
        
    
    # colocar essa coisa na pagina
    # adicionar o titulo na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
 
 # executar o seu sistema 
ft.app(main, view=ft.WEB_BROWSER)
