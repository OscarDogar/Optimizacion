
# coding: utf-8

# In[4]:


funcion = lambda x: x**3 - 3*x +2
der1 = lambda x: 3*x**2 - 3
x0=10
cont=1
error=5e5
while(error>5e-5):
    x1=x0-funcion(x0)/der1(x0)
    error=abs((x1-x0)/x1)
    x0=x1
    print("Contador",cont," X0 = ",x0," X1 = ",x1," Error = ",error)
    cont+=1

