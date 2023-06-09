#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pandas_valuematcher(matcher, df, col):
    '''function to search pandas dataframe for specific 
    patterns and return a new dataframe only of matchers
    matcher=regex to match (use r'matcher' format in func), 
    df=target df, col=column to search'''
    
    import pandas as pd
    
    def delist(args):
        delist = [var for small_list in args for var in small_list]
        return(delist)
    
    match_pattern = re.compile(matcher)
    
    indexer_list = []
    for var in df.iloc[:,col]:
        match_finder = match_pattern.findall(var)
    
        if len(match_finder) > 0:
            indexer = df.index[df.iloc[:,col] == ''.join(match_finder)].to_list()
            indexer_list.append(indexer)
    
    df_match = []
    for var in delist(indexer_list):
        target = df.iloc[var]
        df_match.append(target)
    
    df_matcher = pd.DataFrame(df_match)
    return df_matcher


# In[ ]:




