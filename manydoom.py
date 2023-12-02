import os
import time
import pygetwindow as gw
import pyautogui

n = 100

def launchChocolateDoom(n: int):
    for i in range(n):
        os.system(f'start C:\chocolate-doom-3.0.1-win32\chocolate-doom.exe -nosound -nosfx -geometry 320x240 -iwad C:\chocolate-doom-3.0.1-win32\doom.wad')

def resize_and_tile_windows(title: str, width: int, height: int, n: int):
    time.sleep(10) #wait for windows to open
    windows = gw.getAllWindows()

    # Screen dimensions
    screen_width, screen_height = pyautogui.size()    

    #calculate number of windows per row and column
    xDistanceBetweenTiles = 175
    yDistanceBetweenTiles = 240

    x=0
    y=0
    w=0

    xPosition=0
    yPosition=0

    # i counts the total number of windows (including VSCode & Task Manager) but we only want DOOM windows.
    # So using w below inside if condition for Doom Window
    # I'm not used to Python so I didn't have a graceful way to remove the unused i varible from the loop    
    for i,window in enumerate(windows[:n+3]): # Added 3 to n value since I also expect 2 more open (non-Doom) windows while running
        if window.title.startswith(title):
            try:
                xPosition = xDistanceBetweenTiles * x
                
                if (xPosition > (screen_width - width)): #if we reach the end of the screen width start a new vertical row
                    x = 0
                    xPosition = 0
                    y += 1
                    
                    yPosition = yDistanceBetweenTiles * y
                    
                    if(yPosition > (screen_height - height)): #if we reach the end of the screen height start back from 0,0
                        yPosition=0
                        y=0                                  
                
                window.moveTo(xPosition,yPosition)
                
                x += 1
                w += 1                 
            except Exception as e:
                print(f"Error managing window: {e}")

launchChocolateDoom(n)
resize_and_tile_windows("The Ultimate DOOM", 320, 240, n)
