#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


#1 How do you load the IMDb dataset into a pandas DataFrame.
df=pd.read_csv(r"c:\Users\Dell\Downloads\IMDB-Movie-Data.csv")


# In[15]:


#2  Display the first 5 rows of the dataset. What information can you gather from these rows?
df.loc[1:5]


# In[16]:


#3. What method would you use to get an overview of column data types and missing values.
#3.1 info() method
df.info()


# In[17]:


#4  Identify the columns with missing values. What strategies can you use to handle them?
# missing values
df.isnull().sum()
# strategies we can use to handle them are 1.drop 2.replace


# In[18]:


#5 Which columns are essential for analyzing movie ratings and details? How would you drop the rest?
df[['Rank','Title','Genre','Rating']]


# In[19]:


#6 Calculate the average runtime of movies in the dataset.
print("Average run time of movies:")
df['Runtime (Minutes)'].mean()


# In[20]:


#7 Count the number of movies in each genre. How can you present this information visually?
pd.set_option('display.max_rows',None)
df.value_counts(subset=['Genre'])


# In[21]:


#8  Who are the top 5 directors with the most movies in the dataset?
df.value_counts(subset=['Director'])[0:5]


# In[22]:


#9 Create a line plot showing the number of movies released each year.
import matplotlib.pyplot as plt


# In[43]:


(df.value_counts(subset=["Year"]))
x=[2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006]
y=[297,127,98,91,64,63,60,51,52,53,44]
plt.plot(x,y)
plt.xlabel("Year")
plt.ylabel("no. of movies")
plt.show()


# In[98]:


#9
ax = df["Year"].value_counts().plot(kind='line')
plt.show()


# In[53]:


#10 Draw a histogram depicting the distribution of movie runtimes.
df['Runtime (Minutes)'].plot(kind='hist', title='Runtime (Minutes)')



# In[72]:


#11 Plot a histogram showcasing the distribution of movie ratings.
df['Rating'].plot(kind='hist', title='Rating')


# In[65]:


#df.sort_values(ascending=False)[0:5]


# In[4]:


#12. Calculate the correlation coefficient between movie ratings and runtimes.
print("correlation coefficient between movie ratings and runtime is:")
df['Rating']. corr(df['Runtime (Minutes)'])


# In[99]:


#13. Identify the 3 most frequent actors in the dataset.


# In[13]:


#14.Is there any visible relationship between box office earnings and movie ratings?
y=df['Rating']. corr(df['Revenue (Millions)'])
print("yes there is positive relationship between  box office earnings and movie ratings:",y)


# In[ ]:


#1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# 28. Analyze the relationship between the number of votes and movie ratings


# In[75]:


x=df['Votes']


# In[76]:


y=df['Rating']


# In[80]:


plt.scatter(x,y,marker='*')
plt.show()


# In[81]:


# very highly correlated voting and movie rating


# In[82]:


# 26. Create bar plots to compare metrics like rating, revenue, and budget. What comparisons can you make?
z=df['Revenue (Millions)']


# In[90]:


plt.plot(x,z)
plt.show()


# In[97]:


ax = df["Year"].value_counts().plot(kind='line')
plt.show()


# In[110]:


#.20 Plot the average movie ratings over the years to identify trends.
x=df.groupby(['Year'])['Rating'].mean()


# In[108]:


ax = x.plot(kind='line')
plt.show()


# In[77]:


# 22. Discover the most common director-actor pairs. Who are they?
df.value_counts(subset=['Actors','Director'])[0:3]


# In[123]:


#23 Analyze how movie runtimes have changed over the years. Are movies getting longer or shorter?
ax = y.plot(kind='line')
plt.ylabel('minutes')
plt.show()


# In[121]:


y=df.groupby(['Year'])['Runtime (Minutes)'].mean()


# In[81]:


# 30. Identify any outliers in the movie runtime data. How would you handle them?
Q1 = df['Runtime (Minutes)'].quantile(0.25)
Q3 = df['Runtime (Minutes)'].quantile(0.75)
IQR = Q3 - Q1


# In[82]:


threshold = 1.5
outliers = df[(df['Runtime (Minutes)'] < Q1 - threshold * IQR) | (df['Runtime (Minutes)'] > Q3 + threshold * IQR)]
print(outliers)


# In[53]:


df


# In[133]:


#19 Create a word cloud visualization using movie titles or keywords from descriptions.
from wordcloud import WordCloud
# Start with one review:
text = df.Description[0]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




