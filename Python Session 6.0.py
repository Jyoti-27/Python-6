#!/usr/bin/env python
# coding: utf-8

# ## Let's assume that there is criteria to unlock the certification
# - They should have the 70 % of the attendance.
# - Their score should be more than 300.
# - If they meet both the criteria then they get merit certificate
# - Otherwise they get participation certificate.

# In[ ]:


# First create if else block just interms of the attendance.
Attendance = input(int"Attendance:")


# In[15]:


Attendance = int(input("Attendance:"))
Scores =  int(input("Scores:"))
if(Attendance > 70 and scores > 300):
    print("You will get Merit Certificate")
    print("Eligible for paticipation certificate")
else:
    print("You will not get Merit Certificate")
    print(" You are not Eligible for paticipation certificate")


# In[16]:


if test expression:
    Body of if
    elif test expression:
    Body of elif
    else:
        Body of else


# In[ ]:


attendancePercentage = 80
gradePoints = 290
if attendancePercentage >= 75 and gradePoints >= 300:
    print("Attendance and grade requirement for Merit certificate met")
else: 
    print("Either attendance of grade (or both) insufficient")
    print("Participation certificate only")


# In[38]:


attendancePercentage = 80
gradePoints = 320
if attendancePercentage < 75:
    print("Attendance requirement for Merit certificate not met")
    print("Participation Certificate only")
elif gradePoints < 300:
    print("Attendance requirement for Merit certificate met")
    print("But insufficient grade")
    print("Participation Certificate only")
else:
    print("Attendance requirement for Merit certificate met")
    print("Grade Requirement for Merit Certificate met")


# In[36]:


list1 = ['a','b', 'c']
list2 = ['abc', 'def', 'd','hello']


# ## Using Membership Test
# - in and not in

# In[31]:


list1 = ['a','b', 'c']
if 'c' in list1:
    print("great")
else:
    print("Not great")


# In[41]:


list1 = ['a','b', 'c']
if 'c' not in list1:
    print("great")
else:
    print("Not great")


# In[ ]:




