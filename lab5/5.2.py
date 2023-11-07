import pandas as pd
from math import pi as m
from matplotlib import pyplot as plt

inf = pd.read_csv("test.csv")
inf =inf.head(1000)
print(inf)
n = inf.isnull().sum()
print(inf.groupby(inf["Rooms"]).agg(len))
print(n)
print(inf[inf['LifeSquare'].isnull()])
plt.plot(inf["Id"],inf["Square"])
plt.yscale(value="log")
plt.show()
plt.boxplot(x = inf["HouseYear"])
plt.show()
inf = inf[inf["HouseYear"]>=1933]
plt.boxplot(x = inf["HouseYear"])
plt.show()
inf["LifeSquare"] = inf['LifeSquare'].fillna(3.14 * inf["Square"])
inf["Healthcare_1"] = inf["Healthcare_1"].fillna(inf["Helthcare_2"])
n = inf.isnull().sum()
print(n)
b = inf.pivot_table(inf,index = inf["DistrictId"],columns = inf["Rooms"],aggfunc = len,fill_value=0)
print(b)