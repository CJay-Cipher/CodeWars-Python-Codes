#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from string import punctuation as pt

def pig_it(text):
    return " ".join([x if x in pt else (x[1:] + x[0] + "ay") for x in text.split(" ")])


# In[ ]:


pig_it('Hello world !')     # elloHay orldway !


# In[ ]:


pig_it('Pig latin is cool')    # 'igPay atinlay siay oolcay'


# In[ ]:




