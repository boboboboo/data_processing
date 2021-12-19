import os
import json

def event_data(data):
    with open(data) as f:
        data = json.load(f)
        data_list = []
        for childs in data:
            if childs['event_id']==1500:
                data_list.append(childs)
    return data_list
            
def ps_tree(json_list):
    path_list=[]
    path_list = ["temp"] * 3
    list2 = []
    
    for i in range(len(path_list)):
        list3 = list2.copy()
        path_list[i] = list3

    path_list[0].append('services')
    path_list[1].append('explorer')
    path_list[2].append('wininit')
    for data_list in json_list:
        if data_list['parent_image_path']== r'\Device\HarddiskVolume3\Windows\System32\services.exe':
            #print(data_list['process_guid'])
            path_list[0].append(data_list['process_guid'])
        elif (data_list['parent_image_path']==r'\Device\HarddiskVolume2\Windows\explorer.exe') or (data_list['parent_image_path']==r'\Device\HarddiskVolume3\Windows\explorer.exe'):
            path_list[1].append(data_list['process_guid'])
        elif (data_list['parent_image_path']==r'\Device\HarddiskVolume2\Windows\System32\wininit.exe'):
            path_list[2].append(data_list['process_guid'])
    return path_list
        

def ps_list(json_list, process_tree):
#pass
#    for data_list in json_list:
        #for guid_list in process_tree:
            #if data_list['parent_guid'] in guid_list:
             #   print(data_list['process_guid'])

#    for guid_list in process_tree:
 #       switch=0
  #      for data_list in json_list:
   #         if data_list['parent_guid'] in guid_list:
    #            if switch==0:
     #               print(data_list['parent_guid'])
      #          switch=1
       #         print("---"+data_list['process_guid'])
        #print("")
    for guid in process_tree:
        print(guid[0])
        guid.pop(0)

        for data_b in json_list:
            for guid_data in guid:
                if data_b['process_guid']==guid_data:
                    print("│")
                    print("├─"+os.path.basename(data_b['image_path'])+"/"+data_b['process_guid'])
            #print(guid_data)
                    for data_a in json_list:
                        if data_a['parent_guid']==data_b['process_guid']:
                            print("│　│")
                            #print("│　├──"+data_a['process_guid']+"/"+data_a['image_path'])
                            print("│　├──"+os.path.basename(data_a['image_path'])+"/"+data_a['process_guid'])
                            for data_list in json_list:
                                if data_list['parent_guid'] == data_a['process_guid']:
                                    #print(data_list['parent_guid'])
                                    print("│　│　　│")
                                    #print("│　│　├──"+data_list['process_guid']+"/"+data_list['image_path'])
                                    print("│　│　　├──"+os.path.basename(data_list['image_path'])+"/"+data_list['process_guid'])
                                    for data_i in json_list:
                                        if data_i['parent_guid'] == data_list['process_guid']:
                                            print("│　│　　│　　│")
                                            print("│　│　　│　　├──"+os.path.basename(data_i['image_path'])+"/"+data_i['process_guid'])
                                            #print("│　│　│　├──"+data_i['process_guid']+"/"+data_i['image_path'])
                                            for data_j in json_list:
                                                if data_j['parent_guid'] == data_i['process_guid']:
                                                    print("│　│　　│　　│　　│")
                                                    print("│　│　　│　　│　　├──"+os.path.basename(data_j['image_path'])+"/"+data_j['process_guid'])
                                                    #print("│　│　│　│　├──"+data_j['process_guid']+"/"+data_j['image_path'])
                                                    for data_k in json_list:
                                                        if data_k['parent_guid'] == data_j['process_guid']:
                                                            print("│　│　　│　　│　　│　　│")
                                                            print("│　│　　│　　│　　│　　├──"+os.path.basename(data_k['image_path'])+"/"+data_k['process_guid'])
                                                            #print("│　│　│　│　│　├──"+data_k['process_guid']+"/"+data_k['image_path'])
                                                            for data_l in json_list:
                                                                if data_l['parent_guid'] == data_k['process_guid']:
                                                                    print("│　│　　│　　│　　│　　│　　│")
                                                                    print("│　│　　│　　│　　│　　│　　├──"+os.path.basename(data_l['image_path'])+"/"+data_l['process_guid'])
                                                                    #print("│　│　│　│　│　│　├──"+data_l['process_guid']+"/"+data_l['image_path'])
                                                                    for data_m in json_list:
                                                                        if data_m['parent_guid'] == data_l['process_guid']:
                                                                            print("│　│　　│　　│　　│　　│　　│　　│")
                                                                            print("│　│　　│　　│　　│　　│　　│　　├──"+os.path.basename(data_m['image_path'])+"/"+data_m['process_guid'])
                                                                            #print("│　│　│　│　│　│　│　├──"+data_m['process_guid']+"/"+data_m['image_path'])
                                                                            for data_n in json_list:
                                                                                if data_n['parent_guid'] == data_m['process_guid']:
                                                                                    print("│　│　　│　　│　　│　　│　　│　　│　　│")
                                                                                    print("│　│　　│　　│　　│　　│　　│　　│　　├──"+os.path.basename(data_n['image_path'])+"/"+data_n['process_guid'])
                                                                                    #print("│　│　│　│　│　│　│　│　├──"+data_n['process_guid']+"/"+data_n['image_path'])

data = "final_data.json"
json_list = event_data(data)
process_tree = ps_tree(json_list)
ps_in_list = ps_list(json_list, process_tree)


#for i in json_list:
#    print(i['event_id'])
