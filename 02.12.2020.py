#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ex1 
def min4(a, b, c, d):
    num = [a, b, c, d]
    return(min(num))


# In[ ]:


#ex2
print ("Введите число")
a = int(input())
def my_div(n):
    div = 0
    for k in range (2, n):
        if a % i == 0:
            div = k
    if div == 0:
        return(n)
    else:
        return(div)
print(my_div(n))


# In[ ]:


#ex3
a=int(input())
b=int(input())
def my_sum(a,b):
    if (b>=0):
        while b!=0:
            a+=1
            b-=1
            my_sum(a,b)
    elif (b<0):
        while b!=0:
            a=a-1
            b=b+1
            my_sum(a,b)
    return(a)
print(my_sum(a,b))


# In[ ]:


#ex4
def power(a, p):
    if a**p = power(a , p):
        return a**p
    else:
        return(a*a**(p-1))


# In[ ]:


#ex5
def permute(list):
    

