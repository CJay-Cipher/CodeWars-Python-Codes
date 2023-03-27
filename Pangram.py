#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
A pangram is a sentence that contains every single letter of the 
alphabet at least once. For example, the sentence 
"The quick brown fox jumps over the lazy dog" is a pangram, because 
it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation.
"""


# In[42]:


def is_pangram(s):
    n = "abcdefghijklmnopqrstuvwxyz"
    s = s.replace(" ", "").lower()
    return len([x for x in n if x not in s]) == 0


is_pangram("The quick brown fox jumps over the lazy dog")


# In[ ]:




