#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


bias = 1
X = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
]
w = [
    random.random(),
    random.random(),
    random.random()
]


# In[3]:


def af(num) : #heaviside
    if num >0 :
        return 1
    else :
        return 0


# In[16]:


def noron(instance) :
    x0 = instance[0]
    x1 = instance[1]
    y = instance[2]
    output = af(x0 * w[0] + x1 * w[1] + bias * w[2])
    error = y - output
    w[0] = w[0] + (error * x0)
    w[1] = w[1] + (error * x1)
    w[2] = w[2] + (error * bias)
    return error


# In[17]:


for i in range (100) :
    print ('epoch : ' + str(i))
    for j in X :
        error = noron(j)
        print(error)
    


# In[18]:


print(w)


# In[22]:


x_new = [0.9,0.8]
af(x_new[0] * w[0] + x_new[1] * w[1] + bias * w[2])


# In[ ]:




