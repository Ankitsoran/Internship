#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Write a python program to find the factorial of a number


# In[1]:


number = 9
fact = 1
for i in range(1, number + 1):
    fact = fact * i
print("The factorial of",9,"is",fact)


# In[2]:


num=int(10)
count=0
for a in range(2,num):
    if num%a==0:
        count+=1
if count>=1:
    print(num, "is Composite Number")
else:
    print(num, "is Prime Number")


# In[1]:


my_string="Environment"
if(my_string==my_string[::-1]):
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")


# In[5]:


import math

a = 20
b = 10
math.hypot(a,b)


# In[ ]:


#Python program to count Occurrence of a character in a string
string=input("Test1234")
char=input("T")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The frequency of the ",char,"in the string is: ",count)


# In[ ]:


#print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))


# In[1]:


string=input("Enter the string: ")
char=input("Please enter the char to find frequency of ta character\n")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The frequency of the ",char,"in the string is: ",count)


# In[2]:


string="Enter the string"
char="t"
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The frequency of the ",char,"in the string is: ",count)


# In[5]:


len("Enter the string" )


# In[8]:


str("Enter the string" ).replace("t","a")


# In[ ]:





# In[ ]:




