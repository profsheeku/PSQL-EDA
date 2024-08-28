#!/usr/bin/env python
# coding: utf-8

# #A quick and easy analysis of this dataset to answer the following:
# 
# a) Who removed the most number of posts from the website?
# b) A pie chart of who removes the post from the website
# c) Whose posts were removed most frequently?
# d) Most Popular posts, by awards received
# e) Comments distribution
# d) Conclusion

# In[54]:


#!pip install pandasql


# In[1]:


import numpy as np 
import pandas as pd 

import seaborn as sns 
import matplotlib.pyplot as plt 
import pandasql as ps #sql 
plt.style.use('bmh')
import os



# # **Loading the Data**
# 

# In[2]:


df = pd.read_csv('/home/shivam_singh/Downloads/beautiful_post/r_dataisbeautiful_posts.csv', low_memory=False)
df.head(60)


# In[108]:


df['full_link'][6]


# In[3]:


df.info()


# In[81]:


merged_df.drop(0,inplace=True)


# In[82]:


o=df.groupby('author')['id'].count().reset_index().sort_values(by='id', ascending=False)
#.sort_values(b
#t = pd.concat(o,df['score'])
selected_columns = ['score']
score_df = df.groupby('score')

# Merge the two DataFrames on the 'author' column
merged_df = pd.merge(o,awards_count.sort_values(ascending=False), on='author', how='left')
merged_df


# In[83]:


o=df.groupby('author')['id'].count().reset_index().sort_values(by='id', ascending=False)
#.sort_values(b
#t = pd.concat(o,df['score'])
selected_columns = ['score']
score_df = df.groupby('author')['score']

# Merge the two DataFrames on the 'author' column
merged_df = pd.merge(o,df.groupby('author')['score'].mean(), on='author', how='left')
merged_df


# In[105]:


o=df.groupby('author')['id'].count().reset_index().sort_values(by='id', ascending=False)
#.sort_values(b
#t = pd.concat(o,df['score'])
selected_columns = ['score']
#score_df = df.groupby('author')['score']

# Merge the two DataFrames on the 'author' column
merged_df = pd.merge(o,df.groupby('author')['over_18'].value_counts().sort_values(ascending=False)
, on='author', how='left')
merged_df


# In[84]:


merged_df=merged_df.drop('author',axis=1)


# In[106]:


df.groupby('author')['over_18'].value_counts().sort_values(ascending=False)


# In[85]:


merged_df.drop(0,inplace=True)
merged_df.corr()


# In[86]:


merged_df


# In[87]:


from scipy.stats import pearsonr 
o = merged_df.drop(0)['id']
b = merged_df.drop(0)['score']
l = pearsonr(o,b)


# In[62]:


df.groupby('total_awards_received').count()


# In[67]:


awards_count = df.groupby('author')['total_awards_received'].count()
awards_count.sort_values(ascending=False)


# In[51]:


l


# In[45]:


df.groupby('author')['score'].mean()


# In[34]:


df.groupby('author')['id'].count().reset_index().sort_values(by='id', ascending=False)


# In[35]:


df[df['author']=='jimrosenz']


# In[13]:


grouped_df = df.groupby('author')['score'].mean().reset_index()


# In[33]:


df.score.median()


# In[17]:


grouped_df


# *Checking for Missing values*
# 

# In[58]:


df.isnull().sum().sort_values(ascending=False)


# We can see that there are a lot of missing values in this dataset. However, because the data is being used for Exploratory Purposes, the missing values do not bother us much.

# **Basic Data Exploration**

# In[59]:


df.describe()


# In[60]:


df.iloc[:,7].value_counts()


# In[92]:


df.over_18.replace(True,1,inplace = True)
df.over_18.replace(False,0,inplace = True)
df.over_18.value_counts()



# In[104]:


df.groupby('author')['over_18'].value_counts().sort_values(ascending=False)


# In[91]:


df[df['author']== '[deleted]']['over_18'].value_counts()


# In[39]:


df = df[df['author'] != '[deleted]']


# In[42]:


df.head(60)


# In[63]:


df.author_flair_text.value_counts()


# In[64]:


df.author.value_counts()


# In[65]:


query = """
SELECT
    score,
    total_awards_received,
    created_utc, num_comments,over_18
FROM
    df
"""

correlation_result_1 = ps.sqldf(query, locals())
print(correlation_result_1.corr())


# Based on the information provided, we can conclude that the "score" variable is heavily skewed towards the lower values, based on the quartile distribution.
# 
# This suggests that the majority of the data points have very low scores, with only a small number of data points having high scores. The presence of outliers with a very high score may also suggest that there are some extreme values that are skewing the distribution. 

# In[68]:


query1="""

SELECT
    author,
    COUNT(*) AS total_posts,
    AVG(score) AS avg_score
FROM
    df
GROUP BY
    author
HAVING
    total_posts >= 10
ORDER BY
    avg_score ASC
LIMIT 10
"""
worst_user = ps.sqldf(query1,locals())


# In[69]:


worst_user


#     *Checking who removed the most Posts*

# In[78]:


selected_columns = ['author', 'score', 'title']

h=df[df['over_18']==1][selected_columns]


# In[79]:


h


# In[47]:


removed_posts = """SELECT removed_by, count(distinct id) as posts_removed 
                    FROM df
                    WHERE removed_by is not null
                    GROUP BY removed_by"""
df_removed_posts = ps.sqldf(removed_posts, locals())
df_removed_posts


# In[83]:


plt.figure(figsize=(7,5))
plt.title('COUNTPLOT')
plt.xlabel('Class')
plt.ylabel('Count')
sns.barplot(x=['Under 18', 'Over 18'],y= df.over_18.value_counts(), palette='viridis');



# In[84]:


fig, ax = plt.subplots(1,2, figsize=(14,5))
ax[0].set_title('UNDER_18')
ax[1].set_title('OVER_18')

sns.distplot(df[df['over_18']==0]['title_length'], ax=ax[0], color='steelblue');
sns.distplot(df[df['over_18']==1]['title_length'], ax=ax[1], color='salmon')


# Making a bar graph for the table above

# In[48]:


removed_by = df_removed_posts['removed_by'].tolist()
number_of_removed_posts = df_removed_posts['posts_removed'].tolist()

# Create pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(number_of_removed_posts, labels=removed_by, autopct='%1.1f%%', startangle=90,
       counterclock=False, wedgeprops=dict(width=0.4, edgecolor='w'))

# Add title and legend
ax.set_title('Post Removal', fontsize=20)
ax.legend(title='User', loc='center', bbox_to_anchor=(0.5, -0.1), fontsize=12)


# In[ ]:





# In[80]:


"""h_labels = [x.replace('_', ' ').title() for x in 
            list(df.select_dtypes(include=['int64', 'bool']).columns.values)]

fig, ax = plt.subplots(figsize=(10,6))
_ = sns.heatmap(df.corr(), annot=True, xticklabels=h_labels, yticklabels=h_labels, cmap=sns.cubehelix_palette(as_cmap=True), ax=ax)"""


# We can see that most posts are removed by the moderator, showing that Reddit Moderators, who are generally unpaid, are actively enforcing subreddit rules to regulate their subreddit. 
# The next question is, whose posts were removed most frequently?

# In[81]:


top_removed = """SELECT author, count(id) as number_of_removed_posts
FROM df  
WHERE removed_by is not null
GROUP BY author 
ORDER BY 2 desc 
limit 10"""
df_top_removed = ps.sqldf(top_removed, locals())
df_top_removed


# We can safely omit the first row, as the database categorises "deleted" as an author when it cannot directly attribute a post to an individual. 

# In[52]:


df_top_removed = df_top_removed.drop([0])


# In[82]:


df['title_length'] = df['title'].apply(lambda x: len(str(x)))


# In[53]:


df_top_removed


# Now, lets see the most popular posts, by total_awards_received 
# 

# In[12]:


popular_posts = """SELECT title, total_awards_received as awards_received 
FROM df  
where title != 'data_irl'
order by 2 desc 
limit 10"""
df_popular_posts = ps.sqldf(popular_posts, locals())
df_popular_posts


# In[13]:


worst_users = df[df['removed_by'] == 1]['id'].value_counts()
print(worst_users.head(10))


# # Comments Distribution
# As seen in our quick statistics, an average reddit post has 28 comments. Lets see how the comments are distributed using a bar chart

# In[14]:


subset = df[df['num_comments'] < 28]
sns.histplot(data=subset, x='num_comments', binwidth=1)

# set the plot title and axis labels
plt.title('Number of Comments per Post')
plt.xlabel('Number of Comments')
plt.ylabel('Frequency')

# display the plot
plt.show()


# As we can see, most posts still have less than 5 comments per post. From this, we can conclude that there are posts with an extremely high number of post which takes the mean to a very high value.

# # CONCLUSION
# As we can see from the beginning, the dataset has a lot of outliers. The data, although heavily skewed, is consistent with what we should expect from a social media dataset, as there are very few posts with a lot of likes/awards or comments, while others garner very few peoples eye. 

# In[ ]:




