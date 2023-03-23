#!/usr/bin/env python
# coding: utf-8

# # Transforming graph data to pandas dataframe

# To make a pandas dataframe from the graphdata it is first necessary to import the data. How to do this is explained on: <br> https://github.com/alkem-io/analytics-playground 

# In[1]:


get_ipython().run_line_magic('run', 'Functions.ipynb')


# To use some of the funtions used in this notebook you first need to download the Functions notebook, which is available in jupyter notebook and spyder.

# In[2]:


import pandas as pd
import json
from pandas import json_normalize


# When you have downloaded the matrix as JSON-format, which is used to create the graph. With open you can open the data to make it as a pandas dataframe. <br><br>
# Within the variable_name['nodes'] it is possible to reach the information of the hubs, challenges, opportunities and contributors

# In[3]:


with open('transformed-graph-data.json', 'r') as file:
    variable_name = json.load(file)


# ### Node information

# In[4]:


nodes = variable_name['nodes']


# In[5]:


hubs = json_normalize(nodes['hubs'])


# In[6]:


contributors = json_normalize(nodes['contributors'])


# In[7]:


challenges = json_normalize(nodes['challenges'])


# In[8]:


opportunities = json_normalize(nodes['opportunities'])


# Save the hub, challenge, opportunity and contributors as csv so you can reach them any time necessary

# In[9]:


hubs.to_csv('graph_hubs')
challenges.to_csv('graph_challenges')
opportunities.to_csv('graph_opportunities')
contributors.to_csv('graph_contributors')


# In[10]:


print('column available for the hubs, challenges, opportunities and contributors are:')
for i in hubs.columns:
    print(i)


# In[11]:


print(f'amount of hubs: {len(hubs)}')
print(f'amount of challenges: {len(challenges)}')
print(f'amount of opportunities: {len(opportunities)}')
print(f'amount of contributors: {len(contributors)}')


# ### Edge information

# In[12]:


edges = json_normalize(variable_name['edges'])


# In[13]:


print('column available for the edges are:')
for i in edges.columns:
    print(i)


# The sourceID = source, and targetID=target

# In[14]:


edge_min = edges.drop(['sourceID', 'targetID', 'weight'], axis=1)


# ## Connect sourceID with node names
# the goal for creating this dataframe is to make a dataframe which shows in the rows the different users and in the journeys the communities. The value is 1 if a user is a member of the journey. The only infromation that is kept of the hubs, challenges, opportunity and contributors are the id, name, type and group

# In[15]:


hubs_min = hubs.drop(['nameID','weight','url', 'avatar', 'country', 'city', 'lon', 'lat', 'leadOrgsCount'], axis=1)
challenges_min = challenges.drop(['nameID','weight','url', 'avatar', 'country', 'city', 'lon', 'lat', 'leadOrgsCount'], axis=1)
opportunities_min = opportunities.drop(['nameID','weight','url', 'avatar', 'country', 'city', 'lon', 'lat', 'leadOrgsCount'], axis=1)
users_min = contributors.drop(['nameID','weight','url', 'avatar', 'country', 'city', 'lon', 'lat'], axis=1)


# ### Connect Hubs

# In[16]:


merge = pd.merge(edge_min, hubs_min, left_on='source', right_on='id', how='left')


# In[17]:


amount_hubs_source = len(merge[merge['displayName'].notnull()])
print(f'there are {amount_hubs_source} amount of hubs as a source node')


# In[18]:


merge = merge.drop(['id'], axis=1)


# In[19]:


merge = merge.rename(columns={'displayName':'name Source', 'type_x':'type Edge', 'type_y':'type Source', 
                              'group_y':'group Source', 'group_x':'group Edge'})


# In[20]:


test_amount_hubs_source = len(merge[merge['name Source'].notnull()])
print(f'there should be {amount_hubs_source} amount of rows')
print(f'there are {test_amount_hubs_source} amount of hubs as a source node')


# ### Connect Challenges

# In[21]:


merge2 = pd.merge(merge, challenges_min, left_on='source', right_on='id', how='left')


# In[22]:


amount_challenges_source = len(merge2[merge2['displayName'].notnull()])
print(f'there are {amount_challenges_source} amount of challenges as a source node')


# In[23]:


merge2['name Source'] = merge2['name Source'].combine_first(merge2['displayName'])
merge2['type Source'] = merge2['type Source'].combine_first(merge2['type'])
merge2['group Source'] = merge2['group Source'].combine_first(merge2['group'])


# In[24]:


merge2 = merge2.drop(['id', 'displayName', 'type', 'group'], axis=1)


# In[25]:


test_amount_challenges_source = len(merge2[merge2['name Source'].notnull()])
print(f'there should be {amount_challenges_source+amount_hubs_source} amount of rows')
print(f'there are {test_amount_challenges_source} amount of hubs and challenges as a source node')


# ### Connect Opportunities

# In[26]:


merge3 = pd.merge(merge2, opportunities_min, left_on='source', right_on='id', how='left')


# In[27]:


amount_opportunities_source = len(merge3[merge3['displayName'].notnull()])
print(f'there are {amount_opportunities_source} amount of challenges as a source node')


# In[28]:


merge3['name Source'] = merge3['name Source'].combine_first(merge3['displayName'])
merge3['type Source'] = merge3['type Source'].combine_first(merge3['type'])
merge3['group Source'] = merge3['group Source'].combine_first(merge3['group'])


# In[29]:


merge3 = merge3.drop(['id', 'displayName', 'type', 'group'], axis=1)


# In[30]:


test_amount_opportunities_source = len(merge3[merge3['name Source'].notnull()])
print(f'there should be {amount_opportunities_source}+{+amount_challenges_source}+{amount_hubs_source}={amount_opportunities_source+amount_challenges_source+amount_hubs_source} amount of rows')
print(f'there are {test_amount_opportunities_source} amount of hubs, challenges and opportunities as a source node')


# ### Connect Contributors

# In[31]:


merge4 = pd.merge(merge3, users_min, left_on='source', right_on='id', how='left')


# In[32]:


amount_users_source = len(merge4[merge4['displayName'].notnull()])
print(f'there are {amount_users_source} amount of challenges as a source node')


# In[33]:


merge4['name Source'] = merge4['name Source'].combine_first(merge4['displayName'])
merge4['type Source'] = merge4['type Source'].combine_first(merge4['type'])
merge4['group Source'] = merge4['group Source'].combine_first(merge4['group'])


# In[34]:


merge4 = merge4.drop(['id', 'displayName', 'type', 'group'], axis=1)


# In[35]:


test_amount_users_source = len(merge4[merge4['name Source'].notnull()])
print(f'there should be {amount_users_source}+{amount_opportunities_source}+{amount_challenges_source}+{amount_hubs_source}={amount_users_source+amount_opportunities_source+amount_challenges_source+amount_hubs_source} amount of rows')
print(f'there are {test_amount_users_source} amount of hubs, challenges, opportunities and contributors as a source node')


# ## Connect targetID with node names

# ### Hubs

# In[36]:


merge5 = pd.merge(merge4, hubs_min, left_on='target', right_on='id', how='left')


# In[37]:


amount_hubs_target = len(merge5[merge5['displayName'].notnull()])
print(f'there are {amount_hubs_target} amount of hubs as a target node')


# In[38]:


merge5 = merge5.rename(columns={'displayName':'name Target', 'type':'type Target', 'group':'group Target'})


# In[39]:


merge5 = merge5.drop(['id'], axis=1)


# In[40]:


test_amount_hubs_target= len(merge5[merge5['name Target'].notnull()])
print(f'there should be {amount_hubs_target} amount of rows')
print(f'there are {test_amount_hubs_target} amount of hubs as a source node')


# ### Challenges

# In[41]:


merge6 = pd.merge(merge5, challenges_min, left_on='target', right_on='id', how='left')


# In[42]:


amount_challenges_target = len(merge6[merge6['displayName'].notnull()])
print(f'there are {amount_challenges_target} amount of hubs as a target node')


# In[43]:


merge6['name Target'] = merge6['name Target'].combine_first(merge6['displayName'])
merge6['type Target'] = merge6['type Target'].combine_first(merge6['type'])
merge6['group Target'] = merge6['group Target'].combine_first(merge6['group'])


# In[44]:


merge6 = merge6.drop(['id', 'displayName', 'type', 'group'], axis=1)


# In[45]:


test_amount_challenges_target = len(merge6[merge6['name Target'].notnull()])
print(f'there should be {amount_challenges_target}+{amount_hubs_target}={amount_challenges_target+amount_hubs_target} amount of rows')
print(f'there are {test_amount_challenges_target} amount of hubs and challenges as a target node')


# ### Opportunities

# In[46]:


merge7 = pd.merge(merge6, opportunities_min, left_on='target', right_on='id', how='left')


# In[47]:


amount_opportunities_target = len(merge7[merge7['displayName'].notnull()])
print(f'there are {amount_opportunities_target} amount of challenges as a source node')


# In[48]:


merge7['name Target'] = merge7['name Target'].combine_first(merge7['displayName'])
merge7['type Target'] = merge7['type Target'].combine_first(merge7['type'])
merge7['group Target'] = merge7['group Target'].combine_first(merge7['group'])


# In[49]:


merge7 = merge7.drop(['id', 'displayName', 'type', 'group'], axis=1)


# In[50]:


test_amount_opportunities_target = len(merge7[merge7['name Target'].notnull()])
print(f'there should be {amount_opportunities_target}+{amount_challenges_target}+{amount_hubs_target}={amount_opportunities_target+amount_challenges_target+amount_hubs_target} amount of rows')
print(f'there are {test_amount_opportunities_target} amount of hubs challenge and opportunities as a target node')


# ### Contributors

# In[51]:


merge8 = pd.merge(merge7, users_min, left_on='target', right_on='id', how='left')


# In[52]:


amount_users_target = len(merge8[merge8['displayName'].notnull()])
print(f'there are {amount_users_target} amount of contributors as a target node')


# In[53]:


merge8 = merge8.drop(['id', 'displayName', 'type', 'group'], axis=1)


# ## Exporting dataframe to csv

# In[54]:


merge8.to_csv('graphdata_pandas.csv', index=False)


# In[55]:


print('column available for the dataframe are:')
for i in merge8.columns:
    print(i)


# # Making predition tabel

# In[56]:


data = pd.read_csv('graphdata_pandas.csv')


# type of the node goes next to the name, this makes it easier to see what type a node is

# In[57]:


for i in range(len(data)):
    data['name Source'][i] = data['name Source'][i] + str(" ") + data['type Source'][i]
    data['name Target'][i] = data['name Target'][i] + str(" ") + data['type Target'][i]


# In[58]:


data[data['name Source']==data['name Target']]


# There arent any source nodes and target nodes that refer to themselfes

# In[59]:


data['type Source'].value_counts()


# In[60]:


data['type Target'].value_counts()


# This seems like a lot of different journeys and contributors, but every connection a user has is put on a different row, so if a user is a member of four different communities, it is counted as 4 different users.

# ## Creating graph

# In[61]:


import networkx as nx
import matplotlib.pyplot as plt
import inspect


# With the what_to_graph function you can graph whatever group or individual you want. <br> The function has the following parameters:

# In[62]:


inspect.getfullargspec(what_to_graph)


# For what you can choose 'all', 'group' or 'individual'. All will allow you to graph the entire dataset, with group you would graph a group which is defined in the pandas dataframe and with individual you can graph an individual, this can be a hub, challenge, opportunity or contributor. <br><br> Once you have defined what you want to graph it is neccessary to define the group_id or the name_id in case you choose to graph a group or individual. If you choose 'all' then you do not need to define any more parameters. <br><br> Next you need to make sure you also define what node_type you want to graph. The option availble are: '', 'Target' or 'Source'. You only need to define this when you choose to graph a group or individual. If you choose to graph all then choose '' for node_type.

# **for privacy reasons the graphs are not shown in this notebook, if you want to use them make sure you delete the '#' in front of the code**
# <br>Examples of how you can use the what_to_graph function:

# In[63]:


#G = what_to_graph(what='group',group_id='6d2fb355-5f0f-4545-b2d1-945f37ecbbb5', node_type='Target')


# In[64]:


#T = what_to_graph(what='individual',name_id='6d2fb355-5f0f-4545-b2d1-945f37ecbbb5', node_type='Target')


# In[72]:


#A = what_to_graph(what='all', node_type='')


# These are the same ids but create a different graph, on indivdual level it shows what is connected with the searched item. With the group the graph shows everything that is connected around this community.

# ## Transform created graph to pandas dataframe

# In order to finally create the dataframe with users in the rows and journeys in the columns you need to make a matrix from the created graph. In this example the dataframe is created from the A graph which is the graph that uses the entire dataset, so all the contributors and journeys are in here.

# In[66]:


df_graph = nx.to_pandas_adjacency(A)
df_graph.index = A.nodes()
df_graph.columns = A.nodes()


# In[67]:


df_graph.shape
print(f'amount of rows: {df_graph.shape[0]}\namount of columns:{df_graph.shape[1]}')


# ## If you want to have only the contributors in the rows and journeys in columns:

# ### delete contributors from columns

# In[68]:


for i in range(len(df_graph)-1, -1, -1):
    if (lastWord(df_graph.columns[i]) == 'user') or (lastWord(df_graph.columns[i]) =='organization'):
        df_graph = df_graph.drop(df_graph.columns[i], axis=1)


# In[69]:


df_graph.shape
print(f'amount of rows: {df_graph.shape[0]}\namount of columns:{df_graph.shape[1]}')


# ### delete communities from rows

# In[70]:


for i in range(len(df_graph)-1, -1, -1):
    if (lastWord(df_graph.index[i]) == 'hub') or (lastWord(df_graph.index[i]) =='challenge') or (lastWord(df_graph.index[i]) =='opportunity'):
        df_graph = df_graph.drop(df_graph.index[i])


# In[71]:


df_graph.shape
print(f'amount of rows: {df_graph.shape[0]}\namount of columns:{df_graph.shape[1]}')


# Now you have created a pandas dataframe with the contributors on the rows and the journeys on the columns. It shows which contributor has a connection with what journey. This dataframe is used as the base of making predictions for the recommendations. :)
