import yaml

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


with open('config.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    #x = int(input("Enter x: "))
    #print('Your x equals: ', x)
    
    a = data['a']
    b = data['b']
    
    x = np.arange(-15, 15, 2.0)
    y = a * ((x - 3)**2) + b

    print('Your final result equals: ', y)




# Data for plotting
t = np.arange(-100, 100, 0.02)
s = a * ((t-3)**2) + b

fig, ax = plt.subplots()
ax.plot(t, s)
ax.scatter(x, y, color = 'red')
ax.grid()

fig.savefig("test.png")
plt.show()

