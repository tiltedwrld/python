#!/usr/bin/env python
# coding: utf-8

# In[21]:


print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
if (a > b):
    x = list(range(b, a+1 ,1))
    print(x)
else:
    x = list(reversed(range(a, b+1, 1)))
    print(x)


# In[23]:


print('Введите 4-значное число')
a = int(input())
print('Введите второе 4-значное число')
b = int(input())
if (a>b):
    a,b=b,a
for i in range(a,b+1):
  if ((i // 1000) == (i % 10)) and (((i // 100) % 10) == ((i % 100) // 10)): 
    print(i)


# In[ ]:




