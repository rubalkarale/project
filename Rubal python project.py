#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[32]:


df=pd.read_csv("Diwali Sales Data.csv",encoding="unicode_escape")


# In[33]:


df


# In[34]:


df.shape


# In[35]:


df.head()


# In[36]:


df.info()


# In[37]:


## drop the column
df.drop(["Status","unnamed1"],axis=1,inplace=True)


# In[16]:


df.info()


# In[13]:


pd.isnull(df)


# In[15]:


df.isnull().sum()


# In[17]:


df.shape


# In[18]:


df.dropna(inplace=True)


# In[19]:


df.shape


# In[20]:


df.info()


# In[22]:


df.isnull().sum()


# In[27]:


## to change the datatype flot into int
df["Amount"]=df["Amount"].astype("int")


# In[28]:


df["Amount"].dtype


# In[29]:


df.columns


# In[38]:


# rename the column as temprory (inplace=True its permantaly chang the name)
df.rename(columns={"Marital_Status":"shaadi"})


# In[39]:


df.describe()


# In[40]:


df[["Age","Marital_Status","Orders"]].describe()


# # EDA

# In[43]:


df.columns


# In[46]:


ax=sns.countplot(x="Gender",data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[50]:


df.groupby(["Gender"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)


# In[48]:


sales_gen = df.groupby(["Gender"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(x="Gender",y="Amount",data=sales_gen)


# # Age

# In[51]:


df.columns


# In[52]:


ax = sns.countplot(data=df,x="Age Group",hue="Gender")
for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


sales_age = df.groupby(["Age Group"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(x="Age Group",y="Amount",data=sales_age)


# # State

# In[56]:


df.columns


# In[82]:


sales_state=df.groupby(["State"], as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False)
sns.set(rc={"figure.figsize":(20,5)})
sns.barplot(data=sales_state,x ="State",y="Orders")


# In[63]:


df.State


# In[72]:


unique_values=df["State"].unique()


# In[73]:


unique_values


# In[80]:


count_values=df["State"].nunique()


# In[81]:


count_values


# In[84]:


state_amount=df.groupby(["State"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.set(rc={"figure.figsize":(25,5)})
sns.barplot(data=state_amount,x ="State",y="Amount")


# # Marital Status

# In[90]:


ax=sns.countplot(data=df,x="Marital_Status")

sns.set(rc={"figure.figsize":(2,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[91]:


## Mostly shoping by marital female


# # Occupation

# In[99]:


sns.set(rc={"figure.figsize":(20,5)})
ax=sns.countplot(data=df,x="Occupation")


for bars in ax.containers:
    ax.bar_label(bars)


# In[102]:


ocupation_amount=df.groupby(["Occupation"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.set(rc={"figure.figsize":(25,5)})
sns.barplot(data=ocupation_amount,x ="Occupation",y="Amount")


# In[103]:


# most buyers are in IT sector,Helthcare,Aviation


# # Product category

# In[107]:


sns.set(rc={"figure.figsize":(30,5)})
ax=sns.countplot(data=df,x="Product_Category")


for bars in ax.containers:
    ax.bar_label(bars)


# In[110]:


product_category_amount=df.groupby(["Product_Category"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.set(rc={"figure.figsize":(30,5)})
sns.barplot(data=product_category_amount,x ="Product_Category",y="Amount")


# In[109]:


## most product category in food,clothing,electronics category


# In[116]:


productId_orders=df.groupby(["Product_ID"], as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(10)
sns.set(rc={"figure.figsize":(20,5)})
sns.barplot(data=productId_orders,x ="Product_ID",y="Orders")


# In[117]:


## it is same like above products_ID by orders nlargest 10 just writing steps different
fig1, ax1=plt.subplots(figsize=(12,7))
df.groupby("Product_ID")["Orders"].sum().nlargest(10).sort_values(ascending=False).plot(kind="bar")


# # Conclusion:
Married women age group 26-35yrs,married women from UP,Maharastra and Karnataka working in IT,Helthcare,Aviation are most likely to buy products are Food,Clothing,Electronic category.
# # Thank you

# In[ ]:




