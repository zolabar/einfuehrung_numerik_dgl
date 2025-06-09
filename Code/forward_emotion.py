#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot, scatter


# In[2]:


g = 9.81
x0 = 0
v0 = 2.6


# ## Settings

# In[3]:


t_max = 0.5 # eigentlich 5.5
n =  100
dt = t_max/n

t = np.linspace(0, t_max, n+1)
index_list = np.linspace(0, n-1, n, dtype=int)


# ## Solving

# In[4]:


v = [v0]
vk = v0

for k in index_list:
    vk_plus_1 = -dt*g + vk
    v.append(vk_plus_1)
    vk = vk_plus_1

v = np.array(v)


# ## Postprocessing

# In[5]:


scatter(t, v)
plt.grid(True)
plt.show()

# ### Vorzeichenwechsel der Geschwindigkeit

# In[6]:


index_min = np.argmin(abs(np.array(v)))
print(t[index_min])


# ## Weg

# In[7]:


x = [x0]
xk = x0
for k, time in enumerate(np.linspace(0, n-1, n, dtype=int)):
    xk_plus_1 = dt*v[k] + xk
    x.append(xk_plus_1)
    xk = xk_plus_1


# In[8]:


scatter(t, x)
plt.show()

print(np.array(x).max())

