#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ex_1
print('Введите числа через пробел')
a = [int(i) for i in input().split()]
a_list = list(a)
print(a_list)
print("Чётные числа списка:")
for i in a_list:
    if int(i) % 2 == 0:
        print(i, end=' ')


# In[ ]:


#ex_2
a = [int(i) for i in input().split()]
a_list = list(a)
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))


# In[ ]:


#ex_3
print('?')
mySet = input()
a = mySet.split(' ')
words = [item for item in a]
my_set = set(words)
print(len(my_set))


# In[ ]:


#ex_4
print('?') #коррекция слепого ввода
set_1 = input()
a1 = set_1.split(" ")
r1 = [int(item1) for item1 in a1]
l1 = set(res1)
print'?'
set_2 = input()
a2 = set_2.split(" ")
r2 = [int(item2) for item2 in a2]
l2 = set(r2)
set(l1).intersection(set(l2))

