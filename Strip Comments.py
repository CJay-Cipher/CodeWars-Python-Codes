#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
Complete the solution so that it strips all text that follows any of a set of comment
markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
print()


# In[252]:


def strip_comments(strng, markers):
    strng = strng.split("\n")
    for x in range(len(strng)):
        var = ""
        for y in strng[x]:
            if y in markers:
                break
            var += y
        strng[x] = var.rstrip()
    return "\n".join(strng)
            
strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas"


# In[1]:


# ChatGPT code

def solution(input_str, markers):
    lines = input_str.split('\n')  # split input string into lines
    for i in range(len(lines)):
        for marker in markers:
            if marker in lines[i]:
                lines[i] = lines[i].split(marker)[0].rstrip()  # strip text after the marker and any whitespace at the end
    return '\n'.join(lines)  # join lines back together with newline characters


# In[4]:


# solution('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
# solution("\n", []) == "\n"
solution(' a #b\nc\nd $e f g', ['#', '$']) #== ' a\nc\nd'


# In[8]:


# Trust code

def solution(sentence: str, markers: list):
    sentence = sentence.splitlines()
    for i in range(len(sentence)):
        for marker in markers:
            ind = sentence[i].find(marker)
            if ind != -1:
                sentence[i] = sentence[i][:ind].rstrip()

    return "\n".join(sentence)


# In[9]:


solution(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd'


# In[ ]:




