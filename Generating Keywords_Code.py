#!/usr/bin/env python
# coding: utf-8

# In[1]:


# List of words to pair with products
words = ['buy', 'discount', 'promotion', 'cheap', 'offer', 'purchase', 'sale']

# Print list of words
print(words)


# In[2]:


products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
print(keywords_list)


# In[3]:


# Load library
# ... YOUR CODE FOR TASK 3 ...
import pandas as pd

# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it
# ... YOUR CODE FOR TASK 3 ...
print(keywords_df.head())


# In[4]:


# Rename the columns of the DataFrame
keywords_df.columns = ['Ad Group', 'Keyword']


# In[5]:


# Add a campaign column

keywords_df['Campaign'] = 'SEM_Sofas'


# In[6]:


# Add a criterion type column

keywords_df['Criterion Type'] = 'Exact'


# In[7]:


# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase

keywords_phrase['Criterion Type'] = 'Phrase'
# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)


# In[8]:


# Save the final keywords to a CSV file
keywords_df_final.to_csv('keywords.csv', index=False)
# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)


# In[ ]:




