from sys import exit


try:
    import cartopy.crs as crs
    import cartopy.feature as cfeature
    print("cartopy module loaded")
except:
    print("No such module like 'cartopy'")
    exit(0)

try:
    import matplotlib.pyplot as plt
    print("matplotlib module loaded")
except:
    print("No such module like 'matplotlib'")
    exit(0)

cities = []
X = []
Y = []

with open("miasta.csv", "r", encoding='utf-8') as data:
    cities_all = data.readlines()

print(cities_all)

for city in cities_all:
    datas = city.split(",")
    cities.append(datas[0].strip())
    X.append(float(datas[1]))
    Y.append(float(datas[2]))

print(cities, X, Y, sep="\n======\n")

# creating window
figure = plt.figure(figsize=(7, 5))
ax = figure.add_subplot(1, 1, 1, projection=crs.Mercator())
ax.stock_img()

ax.set_extent([-10, 35, 66, 34], crs=crs.PlateCarree())

plt.scatter(x=Y, y=X, color="red", s=4, alpha=1, transform=crs.PlateCarree())

plt.show()
