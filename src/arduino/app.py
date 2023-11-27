import serial
# import webbrowser
from time import sleep
import pyautogui

PORT = 'COM7'

arduino = serial.Serial(PORT, 9600)

while True:
  msg_formatted = ""
  msg = str(arduino.readline())
  for i in range(len(msg)):

    if i == 2 or i == 3 or i == 4 or i == 5:
      msg_formatted += msg[i]

  print(msg_formatted)

  if msg_formatted == 'ente':
    pyautogui.press('right') #precisa resolver conflito
    # pyautogui.keyUp('enter')
  elif msg_formatted == 'down':
    pyautogui.press('down')
  elif msg_formatted == 'left':
    pyautogui.press('left')
  elif msg_formatted == 'righ':
    pyautogui.press('right')
  elif msg_formatted == 'sobe':
    pyautogui.press('up')

  arduino.flush()       
          

