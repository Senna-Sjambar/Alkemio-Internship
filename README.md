# Internship Alkemio

During my internship at Alemio I have done research into implementing a recommendation system. To goal is to give users, who are at least member of one community, a relevant recommendation. The recommendation can be a Challenge or Opportunity since these are specific challenges community's are working on. Implementing a recommendation system will allow user to become more aware of other community's that are on the platform. They can make impact or find other relevant information that can be used for their community. 

Different models have been researched and in the end the user-based collaborative filtering method was chosen to implement. This is a transparent model which is based on the principle that similar users to the active user have the same interests. The basics of the model works as follows:
1. calculate the similarity between the active user and all other users. 
2. select an amount of most similar users.
3. recommend community's to the active user based on the selected similar users.

The calculation of the similarities in the first step is done with the Jaccard-index. Selecting the amount of users can be done with a fixed amount of users or by using a threshold, every similar user with a jaccard score above this threshold is then selected as most similar user. Recommending a community can be done by calculating the average or the weighted average based on the interests of the selected similar users. Eventually four models were compared to each other:
1. user-based model with a fixed amount of neighbors and the average
2. user-based model with a fixed amount of neighbors and the weighted sum
3. user-based model with a threshold and the average
4. user-based model with a threshold and the weighted sum

The models were evaluated by looking at the coverage for the users, recall, coverage for the community's and the accuracy in this order from high to low priority. The results of the models were compared to a model which only recommends random community's and a model which only randomly recommends the most populair community's. The community's that were seen as outliers based on the amount of members were considered as most populair.

Eventually the user-based model with a threshold of 0.175 and the weighted average turned out the best according to the evaluation scores. It performed better then all the other models and was able to recommend more community's then only the popular ones. It returned a recall of 79.3% for users how are in at least three or more Challenges and/or Opportunities. This means of all the relevant community's the model was able to recommend 79.3% of those community's. It was able to give every user a recommendation and was able to recommend 62.9% of the community's. Finally it had an accuracy score of 97.5% which means that the community's that were and weren't recommended were 97.5% accurate.

In the end it has been made possible to give users recommendations based on the community's they are member of and visualize the results. The visualization shows a graph with the active users, its community's, the selected similar users and the community's that are eventually recommended. In the map ' Jupyter Notebook' you can find all the notebooks I have used to transforming the orginal data and put it into a prediction matrix and finally to make the recommendations and visualizations. In the notebook 'functions' you will find all the functions I have used during this internship.

I have learned a lot from this expierence and am gratefull that Alkemio gave me this Opportunity.
