#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import init_session


# In[4]:


init_session(use_latex=True)


# In[13]:


x, y, z, t = symbols('x,y,z,t')
funcion = 22*x**3*y**3*z**3 + 13*x**2*y**2*z**2 - 45*x*y**2*z**2 + 34*x**2*y**2*z**2
#el va a operar los valores que sean iguales 
funcion


# In[14]:


Dx = funcion.diff(x)
Dy = funcion.diff(y)
grad = ([Dx,Dy])
grad


# In[17]:


Hessi = ([[funcion.diff(x,2),funcion.diff(x,y)],[funcion.diff(y,x),funcion.diff(y,2)]])
Hessi


# In[20]:


(x,y)=symbols(' x y ')
func = tan(x**2) + csc(4*x - 4*y) + sec(y**2)
func


# In[21]:


grad = ([func.diff(x),func.diff(y)])
grad


# In[22]:


Hessi = ([[func.diff(x,2),func.diff(x,y)],[func.diff(y,x),func.diff(y,2)]])
Hessi


# In[ ]:




