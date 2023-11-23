import serial
import webbrowser
from time import sleep
import pyautogui

PORT = 'COM10'

arduino = serial.Serial(PORT, 9600)

while True:
  cu = ""
  msg = str(arduino.readline())
  for i in range(len(msg)):

    if i == 2 or i == 3 or i == 4 or i == 5:
      cu += msg[i]

  print(cu)
  if cu == 'abre':
    # o cu abriu!
    webbrowser.open("https://dinosaur-game.io")
  elif cu == 'down':
    pyautogui.press('down')
  elif cu == 'left':
    pyautogui.press('left')
  elif cu == 'righ':
    pyautogui.press('right')
  elif cu == 'sobe':
    pyautogui.press('up')

  arduino.flush()
