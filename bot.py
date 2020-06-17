from PIL import ImageGrab
import pyautogui
import keyboard

width, height = pyautogui.size()
centerWidth = 0
centerHeight = 0

def moveMouse(x, y):
    pyautogui.moveTo(x, y)

def getCenterPosition():
    global width
    global height
    global centerWidth
    global centerHeight
    centerHeight = height / 2 ## Pega o centro
    centerWidth = width / 2 ## Pega o centro

def trigger():
    pyautogui.click()

def getEnemyColor():
    global centerHeight
    global centerWidth
    screen = ImageGrab.grab()
    for i in range(int(centerWidth - 60), int(centerWidth + 60)):
        colorA = screen.getpixel((i, centerHeight + 50))
        stringColor = str(colorA)
        possoAtira = False
        for i in range (240, 250):
            if stringColor.find(str(i)+",") != -1:
                possoAtira = True
        if possoAtira == True:
                trigger()

def start():
    print("Python trigger bot\nFunciona somente em modo tela cheia janela")
    getCenterPosition()
    moveMouse(centerWidth, centerHeight)

start()

while(True):
    if keyboard.is_pressed('shift'):
        getEnemyColor()



