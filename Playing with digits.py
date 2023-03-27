#!/usr/bin/env python
# coding: utf-8

# In[55]:


"""
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken 
to the successive powers of p is equal to k * n.

In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""
def dig_pow(n, p):
    z = [int(y) for y in str(n)]
    new = sum([z[x]**(p+x) for x in range(len(z))])
    return int(new/n) if new % n == 0 else -1

print(dig_pow(92, 1))
print(dig_pow(46288, 3))


# In[5]:


3.63 % 3 == 0


# In[ ]:



