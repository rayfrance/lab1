import PySimpleGUI as sg

def calcular_equacao(equacao):
  '''
Recebe:
equacao (str) ->  equação que o usuário deseja obter o resultado, essa equação tem apenas dois operandos. 
ex: 2 + 4, 2-5, 7*8, 10 -2, 14+ 4, 18%4, 16/5


Retorno:
resultado -> cálculo da equação 
'''
  resultado = 0
  print(equacao + f"\n tipo equacao: {type(equacao)}")
  #COLOQUE SEU CÓDIGO AQUI
  equacao.strip()
  N1 = equacao[0]
  op = equacao[1]
  N2 = equacao[2]

  if (op == '+'):
    resultado = n1+n2
  elif (opr == '-'):
    resultado = n1-n2
  elif (op == '*'):
    resultado = n1*n2
  elif (op == '/'):
    resultado = n1/n2
  elif (op == '%'):
    resultado = n1%n2

  return resultado
 
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text("Calculadora", justification= "center", size=(400,1))],
            [sg.InputText(size=(10,1)), sg.Button("="), sg.Text("         ", size=(0,1), key="print", background_color="green")],
         ]

# Create the Window
window = sg.Window('CalcLab', layout, size= (400,100))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    window['print'].update(str(calcular_equacao(values[0])))


