# Customizando Campos
# Uso de checkbox, slidebuttons e afins

import PySimpleGUI as sg

# Quando rodar os dados aparecerão no terminal


class TelaPython:
    def __init__(self):
        # Layout
        # Serão 3 linhas: 1-Nome 2-Idade 3-enviar
        layout = [
            # sg.Text cria um label, sg.input pega o dado
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0))],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(5, 0))],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail'), sg.Checkbox(
                'Outlook'), sg.Checkbox('Yahoo')],
            [sg.Button('Enviar Dados')]
        ]
        # Janela

        #"Dados do usuário é o nome da janela"
        # sg.layout recebe o layout criado anteriormente
        janela = sg.Window('Dados do usuário').layout(layout)

        # Extrair os dados da tela
        self.button, self.value = janela.Read()

    def Iniciar(self):
        print(self.value)


tela = TelaPython()
tela.Iniciar()
