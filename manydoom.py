import os
import time
import pygetwindow as gw
import pyautogui

n = 1000
x=0
y=0
xPosition=0
yPosition=0
windowTitle = "The Ultimate DOOM"
windowWidth = 320
windowHeight = 240

def resize_and_tile_window():
    
    global n
    global x
    global y
    global xPosition
    global yPosition
    global windowTitle
    global windowWidth
    global windowHeight
    xDistanceBetweenTiles = 40
    yDistanceBetweenTiles = 120

    #Get Screen dimensions
    screen_width, screen_height = pyautogui.size()    
    
    window = gw.getActiveWindow()
    try:
        xPosition = xDistanceBetweenTiles * x
        
        if (xPosition > (screen_width - windowWidth)): #if we reach the end of the screen width start a new vertical row
            x = 0
            xPosition = 0
            y += 1
            
            yPosition = yDistanceBetweenTiles * y
            
            if(yPosition > (screen_height - windowHeight)): #if we reach the end of the screen height start back from 0,0
                yPosition=0
                y=0                                  
        
        window.resizeTo(windowWidth,windowHeight)
        window.moveTo(xPosition,yPosition)
        
        x += 1                     
    except Exception as e:
        print(f"Error managing window: {e}")

def launchChocolateDoom():
    global n

    for i in range(n):
        os.system(f'start C:\chocolate-doom-3.0.1-win32\chocolate-doom.exe -extraconfig C:\chocolate-doom-3.0.1-win32\chocolate-doom.cfg -1 -nosound -nosfx -nomusic -iwad C:\chocolate-doom-3.0.1-win32\doom.wad')
        w = i+1
        print(f"Opening DOOM Window {w}")
        time.sleep(0.100)
        resize_and_tile_window()

launchChocolateDoom()