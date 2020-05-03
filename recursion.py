#!/usr/bin/env python
# coding: utf-8

# In[14]:


# PART I - IMPLEMENT THE FIBONNACI SEQUENCE

def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n - 1) + fibonnaci(n - 2))


# PART II - IMPLEMENT EUCLID’S GCD ALGORITHM

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


# PART III - STRING COMPARISON
                   
def compareTo(s1, s2):
    if s1 > s2:
        return 1
    elif s1 == s2:
        return 0
    elif s1 < s2:
        return -1
    else:
        return compareTo(s1, s2)


# TESTING

print(fibonnaci(7))
print (gcd(60, 48))
print(compareTo("bd", "bc"))


# In[ ]:




