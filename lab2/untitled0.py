# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T-Sl8LKf1nRF_LELAGwAFb-L-8aGVBqw
"""

import numpy as np
import matplotlib.pyplot as plt
group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

fig = plt.figure(figsize =(10, 7))
plt.title("Box Plot A")
plt.ylable("Y axis label")
# Creating plot
plt.boxplot(group_A)

# show plot
plt.show()

figb = plt.figure(figsize =(10, 7))
plt.title("Box Plot B")
plt.ylable("Y axis label")
# Creating plot
plt.boxplot(group_B)

# show plot
plt.show()