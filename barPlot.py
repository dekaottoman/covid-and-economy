import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("newData.csv")

hds = ["Underdeveloped", "Developing", "Developed"]
mrm = []
for s in hds:
    mrm.append(data.loc[data["HDS"] == s, "MR"].mean())
print(mrm)

fig = plt.figure(figsize = (10, 5))
plt.bar(hds, mrm, width = 0.4) 
plt.xlabel("Development Status")
plt.ylabel("Mortality Rate")
plt.title("Development Status and Mortality Rates")
plt.show()

wlhs = ["Extreme Low", "Low", "Moderate", "Moderate High", "Extreme High"]
mrw = []
for s in wlhs:
    mrw.append(data.loc[data["WLHS"] == s, "MR"].mean())
print(mrw)

fig = plt.figure(figsize = (10, 5))
plt.bar(wlhs, mrw, width = 0.4) 
plt.xlabel("Wealth Status")
plt.ylabel("Mortality Rate")
plt.title("Wealth Status and Mortality Rates")
plt.show()