import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('lipid_num_dens.csv', sep = " ", names = ['Z', 'Num'])
df2 = pd.read_csv('prot_area.csv', sep = " ", names = ['Z', 'Area'])

fig, ax1 = plt.subplots()

ax1.plot(df1['Z'], df1['Num'], lw=2, color="blue")
ax1.set_ylabel("Number of lipid atoms", fontsize=16, color="blue")

for label in ax1.get_yticklabels():
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(df2['Z'], df2['Area'], lw=2, color="darkgreen")
ax2.set_ylabel("Area $(\AA^2)$", fontsize=16, color="darkgreen")
for label in ax2.get_yticklabels():
    label.set_color("darkgreen")

ax1.set_xlabel("Z Height $(\AA)$", fontsize=16, color="red")
for label in ax1.get_xticklabels():
    label.set_color("red")


plt.grid()
plt.show()

