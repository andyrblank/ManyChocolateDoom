import os
import time
import pygetwindow as gw
import pyautogui

w = 0
n = 100

def launchChocolateDoom(n: int):
    for i in range(n):
        os.system(f'start C:\chocolate-doom-3.0.1-win32\chocolate-doom.exe -nosound -nosfx -geometry 320x240 -iwad C:\chocolate-doom-3.0.1-win32\doom.wad')

def resize_and_tile_windows(title: str, width: int, height: int, n: int, w: int):
    time.sleep(10) #wait for windows to open
    windows = gw.getAllWindows()

    # Screen dimensions
    #screen_width, screen_height = pyautogui.size()

    #calculate number of windows per row and column
    windows_per_row = 5
    windows_per_column = 20

    # i counts the total number of windows (including VSCode & Task Manager) but we only want DOOM windows.
    # So using w below inside if condition for Doom Window
    # I'm not used to Python so I didn't have a graceful way to remove the unused i varible from the loop    
    for i,window in enumerate(windows[:n+2]): # Added 2 to n value since I also expect 2 more open (non-Doom) windows while running
        if window.title.startswith(title):
            try:
                #window.resizeTo(width, height) #Window is sized by Chocolate Doom
                window.moveTo((w % windows_per_row) * 300, (w // windows_per_column) * 200)      
                w += 1                 
            except Exception as e:
                print(f"Error managing window: {e}")

launchChocolateDoom(n)
resize_and_tile_windows("The Ultimate DOOM", 320, 240, n, w)
