import pandas as pd

import plotly.express as px

from matplotlib import pyplot as plt

# https://www.kaggle.com/datasets/tayyarhussain/best-selling-game-consoles-of-all-time

data = pd.read_csv(r"C:\Users\roberto.junior\Desktop\best_selling_game_consoles.csv")


def grafico_barras(DataBar):
    colors = ["black", (0.33, 0.33, 0.33, 1.0), "gray", (0.66, 0.66, 0.66, 1.0)]
    console_names = DataBar["Console Name"]
    units_sold = DataBar["Units sold (million)"]
    x_ticks = range(len(console_names))

    fig, ax = plt.subplots()
    ax.bar(x_ticks, units_sold, color=colors)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(console_names, rotation=90)
    ax.set_xlabel("Consoles")
    ax.set_ylabel("Unidades Vendidas (Milhão)")
    ax.set_title("Consoles mais vendidos de 1976 a 2020")
    plt.show()


def grafico_temp(DataTemp):
    DataTemp = DataTemp.sort_values(by="Released Year", ascending=True)

    fig, ax = plt.subplots()
    ax.plot(
        DataTemp["Console Name"],
        DataTemp["Released Year"],
        marker="o",
        color="black",
    )
    ax.set_xlabel("Consoles")
    ax.set_ylabel("Ano lançamento")
    ax.set_title("Ano de lançamento dos consoles mais vendidos")
    ax.tick_params(axis="x", rotation=90)
    plt.show()


def grafico_treemap(DataTree):
    company = DataTree["Company"]

    console = DataTree["Console Name"].unique()

    fig = px.treemap(DataTree, path=[company, console])
    fig.show()


grafico_barras(data)
grafico_temp(data)
grafico_treemap(data)
