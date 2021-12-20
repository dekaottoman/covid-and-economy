import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("newData.csv")

cols = "AGE,POR,HDI,GDPCAP,ARRVL,DPRT,TD,TC,POP,MR,SPI,ARI,DPI,TRI".split(',')
for c in cols:
    sns.displot(data[c] , bins=20)
    plt.title(c)
    plt.show()