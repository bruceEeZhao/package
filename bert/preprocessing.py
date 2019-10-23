import pandas as pd
import os
import re

def filter(text):
    html_tags = re.compile('<.*?>')
    text = re.sub(html_tags, '', text)

    return text

def data_prprocess(train_data_path, label_data_path, test_data_path):
    train_data = pd.read_csv(train_data_path)
    label_data = pd.read_csv(label_data_path)
    # 拼接
    train_data = train_data.merge(label_data, on='id', how='inner')
    # 处理空白内容
    # train_data['label'] = train_data['label'].fillna(-1)
    # train_data = train_data[train_data['label'!= -1]]
    # train_data['content'] = train_data['content'].fillna('无')
    # train_data['title'] = train_data['title'].fillna('无')
    train_data = train_data.dropna()
    train_data['label'] = train_data['label'].astype(int)
    # 数据清洗
    train_data['content'] = train_data['content'].apply(lambda x: filter(x))
    train_data['title'] = train_data['title'].apply(lambda x: filter(x))
    train_data['title_content'] = train_data['title']+train_data['content']
    train_data['Length'] = train_data.title_content.apply(lambda x: len(x))
    
    tmp = train_data[ train_data['Length'] > 50 ]
    del train_data
    train_data = tmp
    # 去除文章中的 \n 字符
    train_data['title_content'].replace('\n', '', regex = True, inplace = True)

    test_data = pd.read_csv(test_data_path)
    test_data['content'] = test_data['content'].fillna('无')
    test_data['title'] = test_data['title'].fillna('无')
    # 数据清洗
    test_data['content'] = test_data['content'].apply(lambda x: filter(x))
    test_data['title'] = test_data['title'].apply(lambda x: filter(x))
    test_data['title_content'] = test_data['title'] + test_data['content']
    # 去除文章中的 \n 字符
    test_data['title_content'].replace('\n', '', regex = True, inplace = True)

    # 训练集分为train set和dev set
    print(train_data.shape)
    size = int(train_data.shape[0] * 0.1) # dev set size
    dev_data = train_data.tail(size)
    train_data = train_data.head(train_data.shape[0] - size)
    print(dev_data.shape)
    print(train_data.shape)

    dev_data.to_csv('./datas/preprocessed_dev_data.csv', index=False)
    train_data.to_csv('./datas/preprocessed_train_data.csv', index=False)
    test_data.to_csv('./datas/preprocessed_test_data.csv', index=False)

if __name__ == "__main__":
    data_prprocess('./origin/Train_DataSet.csv', 
    './origin/Train_DataSet_Label.csv',
    './origin/Test_DataSet.csv')
