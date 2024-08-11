import pyautogui

res = pyautogui.locateOnScreen("powershell.png")

print(res)

powershell_coordinates = pyautogui.center(res)

print(powershell_coordinates)

pyautogui.moveTo(powershell_coordinates)





