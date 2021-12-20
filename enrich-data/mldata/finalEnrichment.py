import pandas as pd

main = pd.read_csv("data.csv")
new = pd.read_csv("newData.csv")

countries = main["COUNTRY"].unique()
for c in countries:
    main.loc[main["COUNTRY"] == c, "GDPCAP"] = new.loc[new["COUNTRY"] == c, "GDPCAP"].max()
    main.loc[main["COUNTRY"] == c, "AGE"] = new.loc[new["COUNTRY"] == c, "AGE"].max()
    main.loc[main["COUNTRY"] == c, "POR"] = new.loc[new["COUNTRY"] == c, "POR"].max()
    main.loc[main["COUNTRY"] == c, "ARRVL"] = new.loc[new["COUNTRY"] == c, "ARRVL"].max()
    main.loc[main["COUNTRY"] == c, "DPRT"] = new.loc[new["COUNTRY"] == c, "DPRT"].max()

#Mortality Rate
for c in countries:
    main.loc[main["COUNTRY"] == c, "MR"] = ((main.loc[main["COUNTRY"] == c, "TD"].max()/main.loc[main["COUNTRY"] == c, "TC"].max())*100)

#Spread Index
for c in countries:
    main.loc[main["COUNTRY"] == c, "SPI"] = main.loc[main["COUNTRY"] == c, "TC"]/main.loc[main["COUNTRY"] == c, "POP"]
 
#Human Development Status
main.loc[main["HDI"] < 0.5 , "HDS"] = "Underdeveloped"
main.loc[(main["HDI"] >= 0.5) & (main["HDI"] < 0.8), "HDS"] = "Developing"
main.loc[main["HDI"] >= 0.8 , "HDS"] = "Developed"

main.loc[main["GDPCAP"] < 2000, "WLHS"] = "Extreme Low"
main.loc[(main["GDPCAP"] >= 2000) & (main["GDPCAP"] < 6000), "WLHS"] = "Low"
main.loc[(main["GDPCAP"] >= 6000) & (main["GDPCAP"] < 24000), "WLHS"] = "Moderate"
main.loc[(main["GDPCAP"] >= 24000) & (main["GDPCAP"] < 44000), "WLHS"] = "Moderate High"
main.loc[main["GDPCAP"] >= 44000, "WLHS"] = "Extreme High"

for c in countries:
    main.loc[main["COUNTRY"] == c, "ARI"] = main.loc[main["COUNTRY"] == c, "ARRVL"]/main.loc[main["COUNTRY"] == c, "POP"]
    main.loc[main["COUNTRY"] == c, "DPI"] = main.loc[main["COUNTRY"] == c, "DPRT"]/main.loc[main["COUNTRY"] == c, "POP"]


wlhs = ["Extreme Low", "Low", "Moderate", "Moderate High", "Extreme High"]
arim = []
dpim = []

for s in wlhs:
    arim.append(main.loc[main["WLHS"] == s, "ARI"].mean())
    dpim.append(main.loc[main["WLHS"] == s, "DPI"].mean())

main["ARI"].fillna(value=0, inplace=True)
main["DPI"].fillna(value=0, inplace=True)

for s, a, d in zip(wlhs, arim, dpim):
    main.loc[(main["ARI"] == 0) & (main["WLHS"] == s), "ARI"] = a
    main.loc[(main["DPI"] == 0) & (main["WLHS"] == s), "DPI"] = d

for c in countries:
    main.loc[main["COUNTRY"] == c, "TRI"] = (main.loc[main["COUNTRY"] == c, "ARI"] + main.loc[main["COUNTRY"] == c, "DPI"])/2

main["ARRVL"].fillna(value=0, inplace=True)
main["DPRT"].fillna(value=0, inplace=True)
main["TC"].fillna(value=0, inplace=True)
main["TD"].fillna(value=0, inplace=True)
main.fillna(main.mean(), inplace=True)

#Groups Based on Death Rates for Classified Prediction
main.loc[main["MR"] <= 1.5 , "MRG"] = 1 #low
main.loc[(main["MR"] <= 2.5) & (main["MR"] > 1.5), "MRG"] = 2 #normal
main.loc[main["MR"] > 2.5 , "MRG"] = 3 #high

#RE-ENGINEERING of features (Due to the way missing data is filled we need to reengineer some of the features)

#Mortality Rate
for c in countries:
    main.loc[main["COUNTRY"] == c, "MR"] = ((main.loc[main["COUNTRY"] == c, "TD"].max()/main.loc[main["COUNTRY"] == c, "TC"].max())*100)

#Spread Index
for c in countries:
    main.loc[main["COUNTRY"] == c, "SPI"] = main.loc[main["COUNTRY"] == c, "TC"]/main.loc[main["COUNTRY"] == c, "POP"]
 
#Human Development Status
main.loc[main["HDI"] < 0.5 , "HDS"] = "Underdeveloped"
main.loc[(main["HDI"] >= 0.5) & (main["HDI"] < 0.8), "HDS"] = "Developing"
main.loc[main["HDI"] >= 0.8 , "HDS"] = "Developed"

main.loc[main["GDPCAP"] < 2000, "WLHS"] = "Extreme Low"
main.loc[(main["GDPCAP"] >= 2000) & (main["GDPCAP"] < 6000), "WLHS"] = "Low"
main.loc[(main["GDPCAP"] >= 6000) & (main["GDPCAP"] < 24000), "WLHS"] = "Moderate"
main.loc[(main["GDPCAP"] >= 24000) & (main["GDPCAP"] < 44000), "WLHS"] = "Moderate High"
main.loc[main["GDPCAP"] >= 44000, "WLHS"] = "Extreme High"

for c in countries:
    main.loc[main["COUNTRY"] == c, "ARI"] = main.loc[main["COUNTRY"] == c, "ARRVL"]/main.loc[main["COUNTRY"] == c, "POP"]
    main.loc[main["COUNTRY"] == c, "DPI"] = main.loc[main["COUNTRY"] == c, "DPRT"]/main.loc[main["COUNTRY"] == c, "POP"]


wlhs = ["Extreme Low", "Low", "Moderate", "Moderate High", "Extreme High"]
arim = []
dpim = []

for s in wlhs:
    arim.append(main.loc[main["WLHS"] == s, "ARI"].mean())
    dpim.append(main.loc[main["WLHS"] == s, "DPI"].mean())

main["ARI"].fillna(value=0, inplace=True)
main["DPI"].fillna(value=0, inplace=True)

for s, a, d in zip(wlhs, arim, dpim):
    main.loc[(main["ARI"] == 0) & (main["WLHS"] == s), "ARI"] = a
    main.loc[(main["DPI"] == 0) & (main["WLHS"] == s), "DPI"] = d

for c in countries:
    main.loc[main["COUNTRY"] == c, "TRI"] = (main.loc[main["COUNTRY"] == c, "ARI"] + main.loc[main["COUNTRY"] == c, "DPI"])/2

main.to_csv("final.csv")
