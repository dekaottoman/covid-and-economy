import pandas as pd
import numpy as np
import scipy.stats as scs
from random import sample

data = pd.read_csv("newData.csv")

mr = data["MR"]
hdi = data["HDI"]
age = data["AGE"]
por = data["POR"]
gdpcap = data["GDPCAP"]
spi = data["SPI"]
tri = data["TRI"]

mrcl = ["AGE", "POR", "HDI", "GDPCAP"]
mrc = [age, por, hdi, gdpcap]
for d, l in zip(mrc, mrcl):
    sp = scs.spearmanr(mr, d)
    pr = scs.pearsonr(mr, d)
    print(l, " - MR\n",sp,"\nPearson : ",pr)

hdicl = ["SPI", "TRI", "GDPCAP"]
hdic = [spi, tri, gdpcap]
for d, l in zip(hdic, hdicl):
    sp = scs.spearmanr(hdi, d)
    pr = scs.pearsonr(hdi, d)
    print(l, " - HDI\n",sp,"\nPearson : ",pr)

gdpcl = ["SPI", "TRI"]
gdpc = [spi, tri]
for d, l in zip(gdpc, gdpcl):
    sp = scs.spearmanr(gdpcap, d)
    pr = scs.pearsonr(gdpcap, d)
    print(l, " - GDPCAP\n",sp,"\nPearson : ",pr)


def getMean (l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    mean = sum / len(l)
    return mean


#Simple Random Sampling for H0
clist = list(data.loc[data["HDS"] == "Developed", "TRI"])
clist = sample(clist,7)
print("Developed Sample : ",getMean(clist), "\nOverall TRI Mean : ", data["TRI"].mean())

#Simple Random Sampling for H1
clist = list(data.loc[data["WLHS"] == "Moderate High", "MR"])
clist = sample(clist,5)
print("Moderate High Sample : ",getMean(clist), "\nOverall MR Mean : ", data["MR"].mean())
