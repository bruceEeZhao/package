import pandas as pd 

res = list()
with open("./mrpc_output/test_results.tsv") as f: 
    lines = f.readlines() 
    for line in lines: 
        line_l = line.split('\t') 
        res.append(line_l.index(max(line_l))) 
            #print(line_l) 

dataframe = pd.read_csv('./origin/Test_DataSet.csv') 
dataframe['label'] = res 
dataframe[['id', 'label']].to_csv('result.csv', index=False, float_format='%.0f') 

