import pyautogui

edge_coordinates = pyautogui.locateCenterOnScreen("Edge_Thumb.png", confidence=0.9)
pyautogui.click(edge_coordinates)

pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
pyautogui.hotkey("Ctrl","t")

pyautogui.write("https://virtusa.com")
pyautogui.hotkey("enter")

