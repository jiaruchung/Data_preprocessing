# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:34:09 2020

@author: jc552
"""
import pandas as pd 

# load text
col_names = ["col1", "col2", "col3"]
data = pd.read_csv(r'C:\Users\jc552\Desktop\WikiQA-test.txt', sep = '\t', header=None, error_bad_lines=False,names=col_names)
print(data)

#filter correct answers only
new_data = data[data['col3'] ==1]
new_data = new_data.drop(["col3"], axis =1)
print(new_data)

#Save
new_data.to_csv(r'C:\Users\jc552\Desktop\final.txt', header=None, index=None, sep='\t')