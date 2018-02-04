
# coding: utf-8

# In[1]:


import sklearn.linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')


# In[2]:


df = pd.read_csv('Gold_prices.csv')
df = df[df.columns[~df.columns.str.contains('Unnamed:')]]
df.columns = ['Date', 'Price']
df.head()


# In[3]:


x = [i for i in range(0,len(df['Price']))] 


# In[4]:


print(df['Price'])


# In[5]:


new_price = []
for i in df['Price']:
    i = i[:2]+i[3:8]
    i = float(i)
    new_price.append(i)    
type(new_price[0])


# In[6]:


#price = df['Price'].tolist()


# In[7]:


df['Price'] = new_price


# In[8]:


(df['Date'][17])


# In[9]:



df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')


# In[10]:


df['Date'][2]


# In[11]:


plt.figure(1)
plt.plot(df['Date'], df['Price'])
plt.show()


# In[12]:


uniq_date =[]
a=1997

while(a<2018):
    for i in range(len(df['Date'])):
        if str(df['Date'][i]).startswith(str(a)+"-08"):
            uniq_date.append(df['Price'][i])
            break
    a += 1


# In[13]:


year = []
for i in range(1997,2018):
    year.append(i)


# In[14]:


slope = []
for i in range(len(uniq_date)-1):
    slope.append(uniq_date[i+1]-uniq_date[i])
slope.insert(0,0.000000)


# In[15]:



df1 = pd.DataFrame(data={'Year':year, 'Price':uniq_date, 'Slope':slope})
df1 = df1[['Year', 'Slope', 'Price']]


# In[16]:


from sklearn.linear_model import LinearRegression
linreg = LinearRegression().fit(df1['Year'].reshape(-1,1), df1['Price'])


# In[17]:


print('(poly deg 2) linear model coeff (w):\n{}'
     .format(linreg.coef_))
print('(poly deg 2) linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))


# In[18]:


pred_prices = []
year = []
for x in range(2022,2023):
    year.append(x)
    pred_prices.append(linreg.predict(x))
year,pred_prices



# In[24]:


plt.figure(2)
plt.plot(df1['Year'], df1['Price'], label = 'Previous Gold Value trends')
plt.scatter(year,pred_prices, c='r', label= 'Predicted Goal Value by 2022')
plt.legend()
plt.show()
