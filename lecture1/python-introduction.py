#!/usr/bin/env python
# coding: utf-8

# In[9]:


# declaring variables
number1 = 1
number2 = 2

string1 = "this is the string 1"
print(number1)
print(number2)
print(string1)


# In[8]:


num1 = 1
num2 = 2
num3 = 3
# putting variables in list
my_list = [num1, num2, num3]
# getting the type of structure
type(my_list)


# In[18]:


# accessing to the element by index number
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list)
# accessing elements in a range
print(my_list[1:2])
# adding and removing elements from list by value
my_list.append(4)
my_list.remove(2)
print(my_list)


# In[21]:


# reversing the list 3,2,1 -> 1,2,3
my_list.reverse()
print(my_list)


# In[31]:


# sorting the list 1,5,2,4 -> 1,2,4,5
my_list.sort()
print(my_list)


# In[34]:


# for loop
for loop_var in range(1,5):
    print(loop_var)


# In[35]:


my_list2 = []
# for loop with range
for loop_var in range(1,10):
    my_list2.append(loop_var)
print(my_list2)


# In[38]:


# finding minimum number in a list
my_list3 = [21, 2, 3, 14, 66, 110, 5, 7, 38]
# just in case the elements can have negative values, we will set the maximum to first element in the list
# if we had set the value of maximum to 0, then negative values would be ignored
maximum = my_list3[0]
for element in my_list3:
    if maximum < element: # change "<" with ">" if you want to find minimum
        maximum = element
print(maximum)        


# In[40]:


i = 0
while(i < 3):
    print(i*2)
    i+=1


# In[45]:


# if the parameters not sent to the function, we will have default values of parameters
def func1(name = "defaultName", surname = "defaultSurname"):
    return name + " " + surname
func1()


# In[50]:


# lambdas are used to define simple functions
getPowerOf2 = lambda num : num * num
print(getPowerOf2(2))

addTwoNum = lambda num1, num2 : num1 + num2
print(addTwoNum(1,7))


# In[59]:


# json like structure -> dictionary
dictionary = {"name" : "ali", "surname" : "karadag", "age" : 25}
type(dictionary)
print(dictionary.values())
print(dictionary.keys())
if("age" in dictionary.keys() and dictionary["age"] > 20):
    print("bigger than 20")

