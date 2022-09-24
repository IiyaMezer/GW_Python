#!/usr/bin/env python
# coding: utf-8

# In[47]:


import sympy
from sympy.plotting import plot




# In[48]:


x = Symbol('X')


# In[49]:


a =18 
b =5
c =10 
d =-30 
f = a*x**3+b*x**2+c*x+d
f


# # Корни

# In[50]:


solveset(f, x, S.Reals)


# Примерно 0.96

# # Находим промежутки возрастания и убывания функции и ее экстремумы

# ## Производная

# In[51]:


d= Derivative(f)
df=d.doit()
df


# In[52]:


print(discriminant(df))


# Дискриминант отрицательный => нет корней => нет точек перегиба => функция монотонна на всей области определения.

# In[53]:


Solve = solveset(df > 0, x , S.Reals )
Solve


# Как видим, производная исходной функции положительна на всей области определения, следовательно, функция возрастает на всей области определения.

# # График

# In[54]:


plot(f, xlim=[-4,4], ylim=[-100,10])
f


# # Промежутки где f > 0  и f < 0 

# Не смотря на то, что из графика и анализа выше и так понятны эти участки, я формлю это надлежшим образом

# In[55]:


positive = solveset(f > 0, x , S.Reals )
positive


# In[56]:


negative = solveset(f < 0, x , S.Reals )
negative

