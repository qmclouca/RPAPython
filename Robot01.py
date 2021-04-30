import pyautogui as p #controle de mouse e teclado

#usar print(p.position()) para encontrar a posição do mouse
# p.sleep(tempo) para dar 2 segundos para posicionar o mouse
# p.sleep(2)
# print(p.position())

# p.moveTo(x=710, y=1056, duration=1)
# p.sleep(1)
# p.click(x=13, y=1068)

p.hotkey('win','r') #combinação de teclas
p.sleep(1)
p.typewrite('notepad', .1)
p.sleep(2)
p.press('enter')
p.sleep(2)
p.typewrite('Oi!! Eu sou um Bot Synnex!', .1)
p.sleep(2)
window = p.getActiveWindow()
window.close()
p.press('right')
p.sleep(2)
p.press('enter')
