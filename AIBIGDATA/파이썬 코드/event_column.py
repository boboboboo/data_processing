import json

def json_load(data):
    with open(data) as f:
        data = json.load(f)

    return data

def save_event_list(data):
    event_id = []

    for i in data:
        event_id.append(i['event_id'])

    event_id = set(event_id)
    event_id = list(event_id)

    return event_id

def save_key_list():
    test = []
    test = ["temp"] * len(event_id)
    list2 = []

    for i in range(len(test)):
        list3 = list2.copy()
        test[i] = list3

    for json_data in data:
        for i, e_id in enumerate(event_id):
            if json_data['event_id']==e_id:
                for j in list(json_data.keys()):
                    test[i].append(j)

    for i in range(len(test)):
        test[i] = set(test[i])
        test[i] = list(test[i])
        test[i].sort()
    return test

def add_key():
    time_list=['event_timestamp', 'process_timestamp', 'image_ctime', 'image_mtime', 'parent_timestamp', 'file_ctime', 'file_mtime', 'src_process_timestamp', 'target_process_timestamp', 'dst_process_timestamp']
    k_test = []
    k_test = ["temp"] * len(event_id)
    k_list2 = []

    for i in range(len(k_test)):
        k_list3 = k_list2.copy()
        k_test[i] = k_list3

    for num, json_data in enumerate(data):
        for i, e_id in enumerate(event_id):
            if json_data['event_id']==e_id:
                data_key = list(json_data.keys())
                data_key.sort()
                if data_key != key_list[i]:
                    lost_key = set(key_list[i]) - set(data_key)
                    for i in lost_key:
                        if i in time_list:
                            data[num][i] = 116444736000000000
                            data[num] = sorted(data[num].items())
                            data[num] = dict(data[num])
                        else:
                            data[num][i] = ""
                            data[num] = sorted(data[num].items())
                            data[num] = dict(data[num])
                            
                            
    return data

data = "final_data.json"

data = json_load(data)
event_id = save_event_list(data)
key_list = save_key_list()
for i in range(len(key_list)-1):
    print(event_id[i], key_list[i])
    
#print(key_list)
#data = add_key()


#with open("fix2.json", "w") as f:
    #json.dump(data, f, indent='\t')

        
        
