#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = ['abcd','qwer','pqrs','ffewsfwef','efewfewfwe']
b = ['badc', 'erqw','pqrs','efwefwefwe','ewfwefwef']
result = [None]*len(a)

for i in range(len(a)):
    if len(a[i])!=len(b[i]):
        result[i] = 'No'
    else:
        la = list(a[i])
        lb = list(b[i])
        even_a = set(la[::2])
        odd_a = set(la[1::2]) 
        even_b = set(lb[::2])
        odd_b = set(lb[1::2])
        
        if odd_a == odd_b:
            # if the sets are equal
            if even_a == even_b:
                result[i] = 'Yes'
            else:
                result[i] = 'No'
        else: 
            result[i]= 'No'
print(result)

