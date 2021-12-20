import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

age = pd.read_csv("./collection/age.csv")
hdi = pd.read_csv("./collection/hdi.csv")
poverty = pd.read_csv("./collection/poverty.csv")
arrival = pd.read_csv("./collection/arrival.csv")
departure = pd.read_csv("./collection/departure.csv")
gdpcap = pd.read_csv("./collection/gdpcap.csv")
population = pd.read_csv("./collection/population.csv")
covid = pd.read_csv("./collection/covid.csv")

main = pd.read_csv("./collection/main.csv")

countries = main["COUNTRY"].unique()
for c in countries:
    main.loc[main["COUNTRY"] == c, "AGE"] = age.loc[age["COUNTRY"] == c, "Median"].max()
    main.loc[main["COUNTRY"] == c, "POR"] = poverty.loc[poverty["country"] == c, "percPoverty"].max()
    main.loc[main["COUNTRY"] == c, "HDI"] = hdi.loc[hdi["country"] == c, "hdi"].max()
    main.loc[main["COUNTRY"] == c, "GDPCAP"] = gdpcap.loc[gdpcap["Country Name"] == c, "2019"].max()
    main.loc[main["COUNTRY"] == c, "ARRVL"] = arrival.loc[arrival["Country Name"] == c, "2016"].max()
    main.loc[main["COUNTRY"] == c, "DPRT"] = departure.loc[departure["Country Name"] == c, "2016"].max()
    main.loc[main["COUNTRY"] == c, "TD"] = covid.loc[covid["COUNTRY"] == c, "TD"].max()
    main.loc[main["COUNTRY"] == c, "TC"] = covid.loc[covid["COUNTRY"] == c, "TC"].max()
    main.loc[main["COUNTRY"] == c, "POP"] = population.loc[population["name"] == c, "pop2020"].max()

#Filling parts of missing data by hand
main.loc[main["COUNTRY"] == "Anguilla", "POR"] = 23.5
main.loc[main["COUNTRY"] == "Anguilla", "HDI"] = 0.865
main.loc[main["COUNTRY"] == "Anguilla", "GDPCAP"] = 18405
main.loc[main["COUNTRY"] == "Andorra", "HDI"] = 0.868
main.loc[main["COUNTRY"] == "Andorra", "POR"] = 0.1
main.loc[main["COUNTRY"] == "Antigua and Barbuda", "POR"] = 18.3
main.loc[main["COUNTRY"] == "Aruba", "POR"] = 15.9
main.loc[main["COUNTRY"] == "Aruba", "HDI"] = 0.908
main.loc[main["COUNTRY"] == "Aruba", "GDPCAP"] = 30253.28
main.loc[main["COUNTRY"] == "Bahamas", "POR"] = 9.3
main.loc[main["COUNTRY"] == "Bahamas", "GDPCAP"] = 28607.90
main.loc[main["COUNTRY"] == "Bahrain", "POR"] = 0.1
main.loc[main["COUNTRY"] == "Brunei", "POR"] = 5
main.loc[main["COUNTRY"] == "Brunei", "GDPCAP"] = 27466.34
main.loc[main["COUNTRY"] == "Barbados", "POR"] = 17.2
main.loc[main["COUNTRY"] == "British Virgin Islands", "GDPCAP"] = 34246
main.loc[main["COUNTRY"] == "British Virgin Islands", "POR"] = 0.1
main.loc[main["COUNTRY"] == "British Virgin Islands", "HDI"] = 0.945
main.loc[main["COUNTRY"] == "Belize", "POR"] = 42
main.loc[main["COUNTRY"] == "Bermuda", "POR"] = 23
main.loc[main["COUNTRY"] == "Bermuda", "HDI"] = 0.981
main.loc[main["COUNTRY"] == "Cabo Verde", "POR"] = 41.3
main.loc[main["COUNTRY"] == "Cabo Verde", "HDI"] = 0.665
main.loc[main["COUNTRY"] == "Cabo Verde", "GDPCAP"] = 3064.27
main.loc[main["COUNTRY"] == "Cabo Verde", "AGE"] = 27.6
main.loc[main["COUNTRY"] == "Cabo Verde", "POP"] = 555988
main.loc[main["COUNTRY"] == "Cuba", "POR"] = 26
main.loc[main["COUNTRY"] == "Dominica", "POR"] = 39
main.loc[main["COUNTRY"] == "Dominica", "HDI"] = 0.724
main.loc[main["COUNTRY"] == "DR Congo", "GDPCAP"] = 556.81
main.loc[main["COUNTRY"] == "Egypt", "GDPCAP"] = 3547.87
main.loc[main["COUNTRY"] == "Eritrea", "GDPCAP"] = 642.51
main.loc[main["COUNTRY"] == "Faroe Islands", "POR"] = 10.1
main.loc[main["COUNTRY"] == "Faroe Islands", "HDI"] = 0.95
main.loc[main["COUNTRY"] == "Gambia", "GDPCAP"] = 787.01
main.loc[main["COUNTRY"] == "Gibraltar", "GDPCAP"] = 92843
main.loc[main["COUNTRY"] == "Gibraltar", "HDI"] = 0.961
main.loc[main["COUNTRY"] == "Gibraltar", "POR"] = 0.1 
main.loc[main["COUNTRY"] == "Grenada", "HDI"] = 0.779
main.loc[main["COUNTRY"] == "Grenada", "POR"] = 32
main.loc[main["COUNTRY"] == "Guadeloupe", "AGE"] = 43.7 
main.loc[main["COUNTRY"] == "Guadeloupe", "POR"] = 34.5
main.loc[main["COUNTRY"] == "Guadeloupe", "HDI"] = 0.853 
main.loc[main["COUNTRY"] == "Guadeloupe", "GDPCAP"] = 24668
main.loc[main["COUNTRY"] == "Guyana", "POR"] = 36.1 
main.loc[main["COUNTRY"] == "Hong Kong", "POR"] = 21.4 
main.loc[main["COUNTRY"] == "Hong Kong", "GDPCAP"] = 46323.86 
main.loc[main["COUNTRY"] == "Iran", "POR"] = 55
main.loc[main["COUNTRY"] == "Iran", "GDPCAP"] = 2282.55 
main.loc[main["COUNTRY"] == "Isle of Man", "HDI"] = 0.849 
main.loc[main["COUNTRY"] == "Isle of Man", "POR"] = 9.3 
main.loc[main["COUNTRY"] == "Isle of Man", "GDPCAP"] = 89112.67
main.loc[main["COUNTRY"] == "Ivory Coast", "GDPCAP"] = 2325.72
main.loc[main["COUNTRY"] == "Kuwait", "POR"] = 0.1 
main.loc[main["COUNTRY"] == "Kyrgyzstan", "GDPCAP"] = 1173.61
main.loc[main["COUNTRY"] == "Laos", "GDPCAP"] = 2630.20
main.loc[main["COUNTRY"] == "Liechtenstein", "GDPCAP"] = 180366.72
main.loc[main["COUNTRY"] == "Liechtenstein", "POR"] = 0.1 
main.loc[main["COUNTRY"] == "Libya", "POR"] = 33.4
main.loc[main["COUNTRY"] == "Monaco", "POR"] = 0.1
main.loc[main["COUNTRY"] == "Monaco", "HDI"] = 1.01
main.loc[main["COUNTRY"] == "Montserrat", "POR"] = 0.1
main.loc[main["COUNTRY"] == "North Macedonia", "AGE"] = 39.1
main.loc[main["COUNTRY"] == "New Zealand", "POR"] = 15
main.loc[main["COUNTRY"] == "Palestine", "AGE"] = 20.8
main.loc[main["COUNTRY"] == "Palestine", "GDPCAP"] = 20.8
main.loc[main["COUNTRY"] == "New Caledonia", "POR"] = 17
main.loc[main["COUNTRY"] == "New Caledonia", "HDI"] = 0.6
main.loc[main["COUNTRY"] == "New Caledonia", "GDPCAP"] = 12579
main.loc[main["COUNTRY"] == "Oman", "POR"] = 25
main.loc[main["COUNTRY"] == "Qatar", "POR"] = 0.1 
main.loc[main["COUNTRY"] == "Russia", "GDPCAP"] = 10126.72
main.loc[main["COUNTRY"] == "South Korea", "GDPCAP"] = 31489.12
main.loc[main["COUNTRY"] == "South Korea", "POR"] = 16.3
main.loc[main["COUNTRY"] == "Saint Kitts and Nevis", "POR"] = 21.8
main.loc[main["COUNTRY"] == "Saint Kitts and Nevis", "GDPCAP"] = 17453
main.loc[main["COUNTRY"] == "San Marino", "HDI"] = 0.961
main.loc[main["COUNTRY"] == "San Marino", "POR"] = 6.7
main.loc[main["COUNTRY"] == "Saudi Arabia", "POR"] = 12.7
main.loc[main["COUNTRY"] == "Singapore", "POR"] = 10
main.loc[main["COUNTRY"] == "Slovakia", "POR"] = 11.9
main.loc[main["COUNTRY"] == "Slovakia", "GDPCAP"] = 19156.89
main.loc[main["COUNTRY"] == "Somalia", "POR"] = 73
main.loc[main["COUNTRY"] == "Somalia", "HDI"] = 0.285
main.loc[main["COUNTRY"] == "South Sudan", "GDPCAP"] = 1119.65 
main.loc[main["COUNTRY"] == "Syria", "GDPCAP"] = 2032
main.loc[main["COUNTRY"] == "Suriname", "POR"] = 47 
main.loc[main["COUNTRY"] == "Taiwan", "POR"] = 1.3 
main.loc[main["COUNTRY"] == "Taiwan", "HDI"] = 0.916
main.loc[main["COUNTRY"] == "Taiwan", "GDPCAP"] = 32787
main.loc[main["COUNTRY"] == "Trinidad and Tobago", "POR"] = 3.7 
main.loc[main["COUNTRY"] == "United Arab Emirates", "POR"] = 19.5
main.loc[main["COUNTRY"] == "Turk and Caicos Islands", "AGE"] = 31 
main.loc[main["COUNTRY"] == "Turk and Caicos Islands", "POR"] =  18
main.loc[main["COUNTRY"] == "Turk and Caicos Islands", "HDI"] =  0.873
main.loc[main["COUNTRY"] == "Turk and Caicos Islands", "GDPCAP"] =  23879
main.loc[main["COUNTRY"] == "Turk and Caicos Islands", "POP"] =  38718
main.loc[main["COUNTRY"] == "Venezuela", "GDPCAP"] =  16055
main.loc[main["COUNTRY"] == "Yemen", "GDPCAP"] =  824

#Mortality Rate
for c in countries:
    main.loc[main["COUNTRY"] == c, "MR"] = ((main.loc[main["COUNTRY"] == c, "TD"]/main.loc[main["COUNTRY"] == c, "TC"])*100)

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

main.to_csv("newData.csv")

print(main.head(20))