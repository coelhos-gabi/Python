from typing import Type
import PySimpleGUI as sg
import sys


class Calculadora:
    def __init__(self):
        layout = [
            [sg.Output(30, 5)],
            [sg.Button('7', size=(5, 0), key='7'), sg.Button('8', size=(5, 0)), sg.Button(
                '9', size=(5, 0)), sg.Button('+', size=(5, 0))],
            [sg.Button('4', size=(5, 0)), sg.Button('5', size=(5, 0)), sg.Button(
                '6', size=(5, 0)), sg.Button('-', size=(5, 0))],
            [sg.Button('1', size=(5, 0)), sg.Button('2', size=(5, 0)), sg.Button(
                '3', size=(5, 0)), sg.Button('x', size=(5, 0))],
            [sg.Button('0', size=(5, 0)), sg.Button('=', size=(5, 0)),
             sg.Button('C', size=(5, 0)), sg.Button('/', size=(5, 0))]
        ]

        janela = sg.Window('Calculadora', resizable=True).layout(layout)
        self.button, self.values = janela.Read()

    def soma(self):
        soma = 0
        soma += self.button

    def Iniciar(self):

        try:
            a = int(input(self.button))
        except ValueError:
            sys.exit(1)
        except TypeError:
            sys.exit(1)


tela = Calculadora()
tela.Iniciar()
