#!/usr/bin/env python
# coding: utf-8

# In[1]:


# create a variable salary and assign a value to it
salary = 15000
if salary >= 35000:
    print('you are eligible for loan')
else:
    print('you are not eligible')


# In[1]:


# lets assume that there is a criteria to unlocl the certifications
- rules
   - they should have 70% of attendance(crtieria 1)
   - score >300(criteria 2)
   - if they meet both the criteria then they get merit certificate 
   - otherwise they  get participation certificate


# In[2]:


# create if else block just in terms of the attendance
attendance = int(input('enter the attendance:'))
score = int(input('enter the score:'))
if attendance >= 70 and score > 300:
    print(' congrats!! you fullfill both the criteria to unlock the merit certification')
else:
    print('your attendance and score is low for merit ceritificate, please collect your participation certificate')


# In[3]:


# if blocks only
attendance = 70
if attendance < 75:
    print("attendance does not fullfill one of the criteria for merit certificate")
    print("you are eligible for participation certificate")


# In[7]:


attendance = 80
if attendance < 75:
    print("Great!! you fullfilled one of the criteria for merit certificate")
    print("you are eligible for participation certificate")


# In[8]:


# check the number is even or odd
num = int(input('enter the number:'))
if num % 2 == 0:
    print( num ,'is an even number')
else:  
    print( num , 'is an odd number') 
    


# # else if ladder
# 
# ## if test expression:
# 
#       Body of if
#      
# ## elif test expression:
# 
#      Body of elif
#     
# ## else: 
# 
#      Body of else
# 

# # using membership test
# - in and not in

# In[9]:


list1 = ['a','b','c']
list2 = ['abc','def','d','hello']


# In[10]:


if 'c' in list1:
    print('great')
else:
    print('not great')


# In[11]:


if 'c' not in list1:
        print('great')
else:
    print('inside else')
    


# ##### More on blocks
# * blocks start below a line ending in :
# * all lines in a block are indented (by 4 spaces)
# * Nested blocks --> nested indenting
# * End of block --> unindent
# 
# 

# In[14]:


marks = int(input('enter the marks:'))
if marks < 40:
    status = 'fail'
    lettergrade = 'F'
else:
     status = 'pass'
     if marks < 50:
        lettergrade = 'D'
     elif marks < 60:
        lettergrade = 'C'
     elif marks < 75:
        lettergrade = 'B'   
     elif marks < 80:
        lettergrade = 'A'   
     elif marks < 90:
        lettergrade = 'A+'   
        
print(status,lettergrade)        


# # Nested if

# In[15]:


number = round(float(input('enter the number:')),2)
if number >= 0:
   if number == 0:
       print('number', number ,'is zero')
   else:
        print('number', number ,'is positive number')   
    
else:
    print('number', number , 'is negative number')


# * Write a code to select a batsman. Below given is the criteria
# * The player should belong to Hyderabad,Bengaluru or Mumbai
# * Player type should be a batsman
# * If he is a batsman he should have scored atleast 5 centuries
# 

# In[16]:


location = ['hyderabad','mumbai', 'begaluru']
player_location = input('enter the location:')
player_type = input('enter the player type :')
no_of_hundreds = int(input('enter the number of hundreds: '))


if player_location in location:
    if player_type.lower() == 'batsmen':
        if no_of_hundreds >= 5:
                print("player is in the squad")
        else:
            print('not selected')
    else: 
        print('we need the batsmen')
else:
    print('location not in the list')


# # write a program to find the grades of a person
# - If the scores is greater than equal to  90 , print grade A
# - If the score is between 80 to 90 then B
# - 80 to 89
#  

# In[17]:


marks = int(float(input('enter the marks obtained: ')))
if marks >= 90:
    print('Grade A')
    
elif marks > 80 and marks <= 89:
    print('Grade B')
    
elif marks > 70 and marks <= 79:
    print('Grade C')
    
elif marks > 60 and marks <= 69:
    print('Grade D')
    
else:
    print('Grade F')    
    


# In[ ]:





# In[ ]:





# In[ ]:




