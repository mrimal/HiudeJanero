
# coding: utf-8

# In[1]:

import pandas as pd
import os

est = "C:\Users\wb474294\Box Sync\DIME\Rio De Janeiro\RAIS_dropbox\Estb2014\Estb2014.TXT"
municipal_code = "C:\Users\wb474294\Box Sync\DIME\Rio De Janeiro\Municipio Codes.txt"


# ### Extract the following variables from Estb2014 data
# + Municpio: municipality code (use Municipio_Codes.csv to retrieve the names)
# + Nomelogradouro: street name 
# + Nmerologradouro: number 
# + Nomebairro: neighboorhood 
# + CEP Estab: zip code

# In[2]:

# Read data
df_est = pd.read_csv(est,sep=';',encoding = 'latin1')
df_mc = pd.read_csv(municipal_code,sep='\t',encoding = 'latin1')


# In[3]:

# print df.columns
print df_est.iloc[:10, [15,16,17,13,1]] 


# In[5]:

print df_mc.columns
print df_mc.iloc[:10, [0,1,2,3,7,8,9]]


# In[11]:

# Extract the relevant columns only
df_address = df_est.iloc[:, [15,16,17,13,1]] 
df_municipio = df_mc.iloc[:, [0,1,2,3,7,8,9]][df_mc.UF==33] #selecting State of Rio only 
print df_address.shape, df_municipio.shape

df_address.columns = ["street_name","street_number","neighborhood","muni_code6","zipcode"]
df_municipio.columns = ["state_code","state","region_code","region","muni_code","muni_code6","municipal"]
df_municipio


# In[12]:

# combine the data together
# df = pd.merge(df_address, df_municipio, how="left", on='municipal_code')
df = pd.merge(df_address, df_municipio, on='muni_code6')
print df.shape
print df[:10]


# In[40]:

# for col in ["street_number","zipcode"]:
#     df[col] = df[col].astype(str)
#     df[col] = df[col].str.strip()

for i in df.zipcode.unique():
    if len(i) <8:
        print i
df.address[df.zipcode=="1045001"]
        
# for col in ["street_name","neighborhood","municipal","state"]:
#     df[col] = df[col].str.strip()


# In[58]:

# df['addr'] = df.street_name.map(str)+" "+df.street_number+", "+df.municipal+" "+df.state_name+", "+df.zipcode
# df['country'] = 'Brazil'
# df['street'] = df.street_name.map(str)+" "+df.street_number


# In[38]:

# # The data set is large so devide it into chunks of n obs
# n = 10000
# # x = df.shape[0]//n
# df_export = df[['addr','zipcode']]

# if not os.path.exists("address"):
#     os.makedirs("address")

# for i in xrange(0, df.shape[0]-n, n):
#     df_export.iloc[i:i+n,:].to_csv('address/address%i-%i.txt'%(i,i+n-1), sep=',',encoding = 'utf-8')
# df_export.iloc[i+n:,:].to_csv('address/address%i-%i.txt'%(i+n,df.shape[0]), sep=',',encoding = 'utf-8')


# In[53]:

# #extract the address part only
# df_export = df[['addr','zipcode']]
# df_export.to_csv('address.txt', sep=',',encoding = 'latin1')


# In[47]:

# len(df['state_name'].unique())
# for x in sorted(df['state_name'].unique()):
#     print x.encode("utf-8")


# In[28]:

# print len(df.municipal.value_counts()), len(df.neighborhood.value_counts())
# df.municipal.value_counts().to_csv('Rio_Municipals.txt', sep=',',encoding = 'latin1')

df['country'] = 'Brazil'
df['street'] = df.street_name.map(str)+" "+df.street_number+" - "+df.neighborhood
df['address'] = df.street_name.map(str)+" "+df.street_number+" - "+df.neighborhood+", "                                                      +df.municipal+" - "+df.state+", "+df.zipcode+", "+df.country


# In[22]:

# Function to devide the data into chunks of n obs and save as csv
def save_addr(n, df, s):
    if not os.path.exists(s):
        os.makedirs(s)

    for i in xrange(0, df.shape[0]-n, n):
        df.iloc[i:i+n,:].to_csv('%s/%s%i-%i.txt'%(s,s,i,i+n-1), sep=',',encoding = 'latin1')
    df.iloc[i+n:,:].to_csv('%s/%s%i-%i.txt'%(s,s,i+n,df.shape[0]), sep=',',encoding = 'latin1')
    
# Function to devide the data by municipals and save as csv
def save_addr_by_municipal(df, s):
    if not os.path.exists(s):
        os.makedirs(s)
        
    for m in sorted(df['municipal'].unique()):
        if m =="Rio de Janeiro":
            save_addr(15000,df[df.municipal==m], s)
        else:
            df[df.municipal==m].to_csv('%s/%s.txt'%(s,m), sep=',',encoding='latin1')
        
    
n = 10000
df_export = df[df.region_code==6].iloc[:,[8,2,5,6,4,7]]
df_export.index = df_export.index - 2711124 #reset index to 0
dirname = "Rio_metro_address"
# save_addr(n,df_export,dirname)
save_addr_by_municipal(df_export,dirname)
# df_export.iloc[0:3000,:].to_csv('0-3000_neighbor.txt', sep=',',encoding = 'latin1')


# In[31]:

print df.columns
print df[df.region_code==6].shape
# df.region.value_counts()
print df[:1]
df.address[0].encode("latin1")


# ### Pending issues:
# + Address sometimes do not exist in google so approximating the location by zipcode nessesary. i.e. Row 1 "RUA JOSE VIEIRA CAULA 5651" (street name does not exist) or Row 6 "RODOVIA  RO -492   KM 101" --> "RO-492 101" (wrong representation?)
# 
# Test using 0-9999: 203 out of 2500 was not mapped by Google API.  
# Neighborhood variable var: 184 out of 2500
# whole address thing: 
# --> To Do: Try incorporate neighboorhood variable to see if improves mapping. Try one-line address for comparison.
# 
# ### Create a pipeline such that:
# 1. first send the whole address
# 2. if error, record that the address didn't work and then try zip code.
