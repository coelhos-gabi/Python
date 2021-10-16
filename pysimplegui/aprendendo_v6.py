# Log de informação na tela

import PySimpleGUI as sg



class TelaPython:
    def __init__(self):
        # Layout
        # Serão 3 linhas: 1-Nome 2-Idade 3-enviar
        layout = [
            # sg.Text cria um label, sg.input pega o dado
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(
                size=(5, 0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox(
                'Outlook', key='outlook'), sg.Checkbox('yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'), sg.Radio(
                'Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # Janela

        #"Dados do usuário é o nome da janela"
        # sg.layout recebe o layout criado anteriormente
        self.janela = sg.Window('Dados do usuário').layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()

            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita_gmail: {aceita_gmail}')
            print(f'aceita_outlook: {aceita_outlook}')
            print(f'aceita_yahoo: {aceita_yahoo}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')


tela = TelaPython()
tela.Iniciar()
