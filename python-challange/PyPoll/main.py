#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import sys


# In[17]:


filepath = "Resources/election_data.csv"


# In[18]:


df = pd.read_csv(filepath)


# In[19]:


df


# In[20]:


total_voters = len(df["Voter ID"].unique())
total_voters


# In[21]:


df["Candidate"].unique()


# In[22]:


Khan = len(df[df["Candidate"] == 'Khan'])


# In[23]:


Correy = len(df[df["Candidate"] == 'Correy'])


# In[24]:


Li = len(df[df["Candidate"] == 'Li'])


# In[25]:


Tooley = len(df[df["Candidate"] == "O'Tooley"])


# In[37]:


Khan_percantage = str((round((Khan / total_voters)*100,3)))+"%"


# In[36]:


Correy_percantage = str((round((Correy / total_voters)*100,3)))+"%"


# In[38]:


Li_percantage = str((round((Li / total_voters)*100,3)))+"%"


# In[39]:


Tooley_percantage = str((round((Tooley / total_voters)*100,3)))+"%"


# In[ ]:





# In[ ]:

filename  = open("pypoll",'w')
sys.stdout = filename

print ("Election Results")
print ("---------------------------------")
print ("Total Votes:"+(str(total_voters)))
print ("---------------------------------")
print ("Khan:"+Khan_percantage+" "+str(Khan))
print ("Correy:"+Correy_percantage+" "+str(Correy))
print ("Li:"+Li_percantage+" "+str(Li))
print ("O'Tooley:"+Tooley_percantage+" "+str(Tooley))
print ("---------------------------------")
print ("Winner: Khan")

