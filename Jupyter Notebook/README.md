# Jupyter Notebook files

In this folder you can find the jupyter notebook files I used. 

To make the recommendation yourself you first need to aquire the data you need to following the steps described here: https://github.com/alkem-io/analytics-playground.

After the data is aquired you need to follow the following steps:
1. Download all the jupyter notebook files provided in this repository
2. Open and run 'Transforming graph data to pandas dataframe 2023' This will allow you to create a pandas dataframe of the graph data. The pandas dataframe will contain all the nodes and edges that are visible in the graph
3. Open and run 'Get ID, name, group and type 2023' This will let you create a dataframe with all the contributors and community's with their ID, name, group and type.
4. Open and run 'Visibilities Hubs 2023' This will create a dataframe with all open community's that are on the platform. This is needed to filter out the closed community's.
5. Open and run 'Transforming pandas dataframe to prediction table 2023' This will transform the dataframe containing the graph data into the prediction table. This contains the contributors as rows and the community's as columns. If a contributor is member of a community it will show the value 1 if not it will show a 0.
6. Open and run 'Make and visualize recommendations 2023' After you have collected all the data and transformed it into useable datasets it is possible to make the recommendations for users that are member of a least one community. Besides returning the name of the recommended community's it is also possible to visualize the connections which lead to the recommended community's. <br><br>

** In the map Newest Version you will find the latest functions which includes making graphs in Alkemio colours and recommend contributors to community's **
