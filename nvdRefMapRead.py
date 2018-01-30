"""
I am building a recipe to import exploit data from the web into python
"""
#Gather the tools
import pandas as pd

#from pandas import DataFrame as df

#Get data
url2 = r'http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html'


#Read in the data
tables2 = pd.read_html(url2)
exploitsDB_table = tables2[3]
exploitsDB_table.columns = ['exploitID','cves']
df2 = pd.DataFrame(exploitsDB_table)


#transform cves column into multiple columns
df3 = df2['cves']
breaker = lambda x: pd.Series([i for i in reversed(x.split('  '))])##Notice there are two spaces here
df4 = df2['cves'].apply(breaker)


#concatenate the two dataframes
df6 = df2['exploitID']
df5 = pd.concat([df6, df4], axis=1, join_axes=[df2.index])


#export the data as csv
path = r'/Users/heathnieddu/Documents/'
df5.to_csv(path+'exploitDB.csv')
