import pandas as pd

import plotly.express as px

from matplotlib import pyplot as plt

# https://www.kaggle.com/datasets/tayyarhussain/best-selling-game-consoles-of-all-time

data = pd.read_csv(r"C:\Users\roberto.junior\Desktop\best_selling_game_consoles.csv")


def grafico_barras(DataBar):
    colors = ["black", (0.33, 0.33, 0.33, 1.0), "gray", (0.66, 0.66, 0.66, 1.0)]

    plt.bar(
        DataBar["Console Name"],
        DataBar["Units sold (million)"],
        color=colors,
    )
    plt.xlabel("Consoles")
    plt.ylabel("Unidades Vendidas (Milhão)")
    plt.title("Consoles mais vendidos de 1976 a 2020")
    plt.xticks(rotation=90)
    plt.show()


def grafico_temp(DataTemp):
    DataTemp = DataTemp.sort_values(by="Released Year", ascending=True)

    plt.plot(
        DataTemp["Console Name"],
        DataTemp["Released Year"],
        marker="o",
        color="black",
    )
    plt.xlabel("Consoles")
    plt.ylabel("Ano lançamento")
    plt.title("Ano de lançamento dos consoles mais vendidos")
    plt.xticks(rotation=90)
    plt.show()


def grafico_treemap(DataTree):
    company = DataTree["Company"]

    console = DataTree["Console Name"].unique()

    fig = px.treemap(DataTree, path=[company, console])
    fig.show()


grafico_barras(data)
grafico_temp(data)
grafico_treemap(data)
