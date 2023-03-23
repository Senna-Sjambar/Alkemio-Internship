#!/usr/bin/env python
# coding: utf-8

# In[3]:


def GetMemberItems(df, member_naam, what_return=['hub', 'challenge', 'opportunity', 'all']):
    all_items = []
    hub_items = []
    challenge_items=[]
    opportunity_items = []
    
    df_small = df[df['user'] == member_naam]
    for i in range(len(df_small.columns)):
        if df_small[df_small.columns[i]].iloc[0] == 1:

            all_items.append(df_small.columns[i]) 
       
    for i in all_items:
        if lastWord(i) == 'hub':
            hub_items.append(i)
        elif lastWord(i) =='challenge':
            challenge_items.append(i)
        elif lastWord(i) == 'opportunity':
            opportunity_items.append(i)
    
    if what_return == 'hub':
        return hub_items
    if what_return == 'challenge':
        return challenge_items
    if what_return == 'opportunity':
        return opportunity_items
    if what_return == 'all':
        return hub_items, challenge_items, opportunity_items
    


# In[ ]:


def GetColName(df, index):
    df = df.T
    df['colnames'] = 0
    df = df.reset_index()
    df = df.rename(columns={"index":"colnames"})
    df = df.iloc[:,:1]
    if index >= len(df):
        print('er is geen column met dit index nummer')
    else:
        naam = df.iloc[index][0]
        return naam


# In[ ]:


def GetUserName(df, index):
#     df_user_index = pd.read_csv('user_index', index_col=0)
    df = df.reset_index()
    df = df.rename(columns={"index":"usernames"})
    df = df.iloc[:,:1]
    if index >= len(df):
        print('er is geen user met dit index nummer')
    else:
        naam = df.iloc[index][0]
        return naam


# In[ ]:


def lastWord(string):
    lis = list(string.split(" "))
    length = len(lis)
    return lis[length-1]


# In[1]:


def what_to_graph(what = ['all','group','individual'], group_id='', name_id='',node_type = ['','Target', 'Source']):
    if what == 'all':
        df = data
    
    if what == 'group':
        if node_type == 'Target':
            df = data[data['group Target']==group_id]
        elif node_type == 'Source':
            df = data[data['group Source']==group_id]
        
    if what=='individual':
        if node_type == 'Target':
            df = data[data['target']==name_id]
        elif node_type == 'Source':
            df = data[data['source']==name_id]

    if df.empty==True:    
        print('search cannot be found')
    else:
        # Create an empty graph
        G = nx.Graph()

        # Add nodes to the graph
        nodes = list(set(df['name Source']).union(set(df['name Target'])))
        for node in nodes:
            category1_matches = df['name Source'] == node
            category2_matches = df['name Target'] == node
            if category1_matches.any() or category2_matches.any():
                category1 = df.loc[category1_matches, 'type Source'].iloc[0] if category1_matches.any() else None
                category2 = df.loc[category2_matches, 'type Target'].iloc[0] if category2_matches.any() else None
                G.add_node(node, category1=category1, category2=category2)

        # Add edges to the graph
        edges = [(row['name Source'], row['name Target']) for index, row in df.iterrows()]
        G.add_edges_from(edges)

        # Define colors for each category
        colors = {'user': 'r', 'organization': 'm','opportunity':'c', 'challenge': 'g', 'hub':'b'}

        # Create a list of node colors based on their categories
        node_colors = [colors[G.nodes[node]['category1']] if G.nodes[node]['category1'] else colors[G.nodes[node]['category2']] for node in G.nodes()]

        # Draw the graph with a larger figure size
        fig = plt.figure(figsize=(20, 16))
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=50, node_color=node_colors)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        plt.axis('off')
        plt.show()
    return G
   


# In[2]:


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# In[ ]:





# In[ ]:




