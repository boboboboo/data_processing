import json
import numpy as np
import pandas as pd
from time import localtime, strftime

def ldap_to_datetime(ldap_time):
    if ldap_time >= 10:
        t = int(ldap_time)
        local=localtime((t/10000000)-11644473600)
        time_format='%Y-%m-%d %H:%M:%S'
        result = strftime(time_format, local)
        return result
    else:
        pass

def create_event_dict(data):
    with open(data) as f:
        data = json.load(f)


    data = pd.DataFrame(data)
    event = data.drop_duplicates(['event_id'])
    event = event[['event_id']]
    event.index = event['event_id'].astype(str)
    event = event.sort_index()
    dict_from_df = event.to_dict()
    dict_from_df = dict_from_df['event_id']

    return dict_from_df


def class_columns(data, columns):
    with open(data) as f:
        data = json.load(f)

    data = pd.DataFrame(data)
    event = data.drop_duplicates(['event_id'])
    event.index = event['event_id'].astype(str)
    event = event.sort_index()
    #test = event.index[event['event_id']==1500]
    #print(event.loc[(event['event_id']==1500)])
    for i in range(len(event.index)):
        #event_copy = event.copy()
        a = event[event.index == event.index[i]].dropna(axis=1)
        a = a.sort_index(axis=1)
        a = a.columns.values.tolist()
        #print(type(a))
        
        #a = event.loc[(event['event_id']==1500)].dropna(axis=1)
        #print(a)
        #print(event.loc[(event['event_id']==1500)].dropna(axis=1))
        columns[i]=a
    return columns

def json_to_list(data):
    with open(data) as f:
        data = json.load(f)

    for childs in data:
        #print(childs['event_id'])
        record = []
        for child in childs:
            record.append(childs[child])
        for i, j in enumerate(save_list):
            if childs['event_id'] == event_id[j]:
                #Test
                if len(record) == len(columns[i]):
                    event_list[i].append(record)
            
    return event_list
        
def list_to_df(json_list):
    for i in range(len(json_list)):
        json_list[i] = pd.DataFrame(json_list[i])
        try:
            time_list=['event_timestamp', 'process_timestamp', 'image_ctime', 'image_mtime', 'parent_timestamp', 'file_ctime', 'file_mtime', 'src_process_timestamp', 'target_process_timestamp', 'dst_process_timestamp']
            json_list[i].columns = columns[i]
            
            for j in time_list:
                if j in json_list[i].columns:
                    json_list[i][j] = json_list[i][j].apply(ldap_to_datetime)
            json_list[i].index = json_list[i]["event_timestamp"]
            #print(json_list[i].index)
            del json_list[i]['event_timestamp']
        except Exception as e:
            print("[Err] Event ID[%s]"%save_list[i], e)
            #test#
            #print(json_list[i].tail(n=1))
    return json_list

def save_to_hdf5(df_list):
    store = pd.HDFStore(hdf5, complib = 'blosc')

    i = 0

    for df in df_list:
        #df.columns = df.columns.astype(str)
        #print(df.columns.map(type))
        df = df.astype("str")
        #print(df.dtypes)
        store["log_"+save_list[i]] = df
        i+=1

    store.close()

    return True

def load_from_hdf5(hdf5_file):
    store = pd.HDFStore(hdf5_file, complib = 'blosc')

    print(store)

    df_list = []
    for df in save_list:
        df_list.append(store["log_"+df])

    store.close()

    return df_list

#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

data = 'testt.json'
hdf5 = 'test.hdf'

event_id = create_event_dict(data)

#print(event_id)
event_list = list(event_id.keys())
columns = ["temp"] * len(event_id.keys())

#print(event_list)

columns = class_columns(data, columns)

''' column list of event id
for i in columns:
    print(i)
'''
#print(columns)
#print(columns[1])
save_list = event_list.copy()

for i in range(len(event_list)):
    event_list[i] = []

json_list = json_to_list(data)

df_list = list_to_df(json_list)


#save_to_hdf5(df_list)
df_list = load_from_hdf5("test.hdf")
#print(df_list[0])
#df_list[0].to_csv('test.csv')

'''
for i, j in enumerate(list(event_id.keys())):
    df_list[i].to_csv("log_{}.csv".format(j))
'''


