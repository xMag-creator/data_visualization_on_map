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
