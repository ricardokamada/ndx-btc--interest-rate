from io import DEFAULT_BUFFER_SIZE
from operator import ne
from tkinter import NS
import pandas as pd
import matplotlib.pyplot as plt

df_BTC = pd.DataFrame(pd.read_csv(
    "./data/BTC_USD Binance Dados Históricos-012021-012022.csv"))
df_NSDX = pd.DataFrame(pd.read_csv(
    "./data/Nasdaq 100 Dados Históricos-012021-012022.csv"))


new = pd.merge(df_BTC, df_NSDX, on=["Data"], suffixes=['_1', '_2'])  # merge

new = new.rename(columns={"Var%_1": "btc_Var%",
                 "Var%_2": "nsdx_Var%"})  # rename

new.drop(['Último_1', 'Abertura_1',  'Máxima_1',  'Mínima_1',   'Vol._1',   'Último_2',
         'Abertura_2',   'Máxima_2',   'Mínima_2',   'Vol._2'], inplace=True, axis=1)  # drop colluns


def plot(x, y):
    fig = plt.figure()
    plt.plot(x, y)
    return fig

f = plot(new['btc_Var%'], new['Data'])
plt.show()

