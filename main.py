import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=1000, y=393)
pyautogui.write("usuario4@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.click(x=977, y=567)
time.sleep(3)  


import pandas as pd

print(pyautogui.position())

tabela = pd.read_csv("produtos.csv")   
for line in tabela.index:
    pyautogui.click(x=1102, y=291)
    codigo = tabela.loc[line, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = str(tabela.loc[line, "obs"]) 
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    