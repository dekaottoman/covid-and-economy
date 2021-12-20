import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("newData.csv")

#Distribution Groups
wlhs = ["Extreme Low", "Low", "Moderate", "Moderate High", "Extreme High"]
hds = ["Underdeveloped", "Developing", "Developed"]

#Wealth Based Ditribution

#Total Population
popw = []
for s in wlhs:
    popw.append(data.loc[data["WLHS"] == s, "POP"].sum())
plt.pie(popw, labels=wlhs)
plt.title("World Population Distribution based on Wealth")
plt.show()

#Total Cases
tcw = []
for s in wlhs:
    tcw.append(data.loc[data["WLHS"] == s, "TC"].sum())
plt.pie(tcw, labels=wlhs)
plt.title("Distribution of Total Cases based on Wealth")
plt.show()

#Total Deaths
tdw = []
for s in wlhs:
    tdw.append(data.loc[data["WLHS"] == s, "TD"].sum())
plt.pie(tdw, labels=wlhs)
plt.title("Distribution of Total Deaths based on Wealth")
plt.show()

#HDI Based Distribution

#Total Population
poph = []
for s in hds:
    poph.append(data.loc[data["HDS"] == s, "POP"].sum())
plt.pie(poph, labels=hds)
plt.title("World Population Distribution based on Human Development")
plt.show()

#Total Cases
tch = []
for s in hds:
    tch.append(data.loc[data["HDS"] == s, "TC"].sum())
plt.pie(tch, labels=hds)
plt.title("Distribution of Total Cases based on Human Development")
plt.show()

#Total Deaths
tdh = []
for s in hds:
    tdh.append(data.loc[data["HDS"] == s, "TD"].sum())
plt.pie(tdh, labels=hds)
plt.title("Distribution of Total Deaths based on Human Development")
plt.show()