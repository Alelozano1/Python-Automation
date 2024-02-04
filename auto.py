import pyautogui as py
import time as t

py.PAUSE = 0.7

py.press("win")
py.write("Chrome")
py.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
py.write(link)
py.press("enter")
py.click(x=759, y=404)
py.write("alexandre-lozano@hotmail.com")
py.press("tab")
py.write("203040")
py.press("enter")

import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    py.click(x=853, y=295)
    py.write(tabela.loc[linha,"codigo"])
    py.press("tab")
    py.write(tabela.loc[linha,"marca"])
    py.press("tab")
    py.write(tabela.loc[linha,"tipo"])
    py.press("tab")
    py.write(str(tabela.loc[linha,"categoria"]))
    py.press("tab")
    py.write(str(tabela.loc[linha,"preco_unitario"]))
    py.press("tab")
    py.write(str(tabela.loc[linha,"custo"]))
    py.press("tab")
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        py.write(obs)
    py.press("enter")   

#         codigo       marca        tipo  categoria  preco_unitario  custo               obs
#0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
#1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
#2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
#3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
#4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
#..          ...         ...         ...        ...             ...    ...               ...
#288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
#289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
#290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
#291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
#292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN