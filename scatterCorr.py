import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv("newData.csv")

#Poverty Rate & Mortality Rate
plt.scatter(data["POR"], data["MR"])
plt.title("Relationship Between Poverty Rate & Mortality Rate (TD/TC)")
plt.ylabel("Mortality Rate")
plt.xlabel("Poverty Rate")
plt.savefig("./graph/scatter/POR-MR.png")
plt.show()

#GDP per capita & Mortality Rate
plt.scatter(data["GDPCAP"], data["MR"])
plt.title("Relationship Between GDP per capita & Mortality Rate (TD/TC)")
plt.ylabel("Mortality Rate")
plt.xlabel("GDP per capita")
plt.savefig("./graph/scatter/GDPCAP-MR.png")
plt.show()

#Human Development Index & Mortality Rate
plt.scatter(data["HDI"], data["MR"])
plt.title("Relationship Between Human Development Index & Mortality Rate (TD/TC)")
plt.ylabel("Mortality Rate")
plt.xlabel("HDI")
plt.savefig("./graph/scatter/HDI-MR.png")
plt.show()

#Mean Age & Mortality Rate
plt.scatter(data["AGE"], data["MR"])
plt.title("Relationship Between Mean Age & Mortality Rate (TD/TC)")
plt.ylabel("Mortality Rate")
plt.xlabel("Mean Age")
plt.savefig("./graph/scatter/AGE-MR.png")
plt.show()

#Human Development Index & Spread Index
plt.scatter(data["HDI"], data["SPI"])
plt.title("Relationship Between Human Development Index & Spread Index (TC/POP)")
plt.ylabel("Spread Index")
plt.xlabel("Human Development Index")
plt.savefig("./graph/scatter/HDI-SPI.png")
plt.show()

#Human Development Index & Travel Index
plt.scatter(data["HDI"], data["TRI"])
plt.title("Relationship Between Human Development Index & Travel Index ((ARI+DPI)/2)")
plt.ylabel("Travel Index")
plt.xlabel("Human Development Index")
plt.savefig("./graph/scatter/HDI-TRI.png")
plt.show()

#Human Development Index & GDPCAP
plt.scatter(data["HDI"], data["GDPCAP"])
plt.title("Relationship Between Human Development Index & GDP per capita")
plt.ylabel("GDP per capita")
plt.xlabel("Human Development Index")
plt.savefig("./graph/scatter/HDI-GDPCAP.png")
plt.show()

#Human Development Index & Poverty Rate
plt.scatter(data["HDI"], data["POR"])
plt.title("Relationship Between Human Development Index & Poverty Rate")
plt.ylabel("Poverty Rate")
plt.xlabel("Human Development Index")
plt.savefig("./graph/scatter/HDI-POR.png")
plt.show()
