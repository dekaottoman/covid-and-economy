import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("newData.csv")

c = data.corr()

print("Correlation of Features")
print(c)
mask = np.triu(np.ones_like(c, dtype=bool))
sns.heatmap(c, mask=mask, cmap="vlag", center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5}, vmin=-1, vmax=1)
plt.title("Correlations of Features")
plt.show()

c.to_csv("./stats/corr.csv")