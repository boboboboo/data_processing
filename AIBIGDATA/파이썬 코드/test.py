import pandas as pd

with open("test.txt") as f:
    data = f.readlines()

id_list = []
for line in data:
    line = line.strip()
    id_list.append(line)
#pd.set_option('display.max_columns', None)
df = pd.read_json("fix3.json")

id_list = set(id_list)
id_list = list(id_list)

#attack_id = df['_id'] == 'b0303d74-3883-4e91-b4fa-4fefe6b2a21c'
#df = df[attack_id]
'''
cnt = 0

for i in id_list:
    if (df['_id'] == i).any() == True:
        cnt += 1
    
print(cnt)
'''

#print((df['tech_id'] == "").any())

    #attack_id = df['_id'] == i
    #test = df[attack_id]
#print(test)
    #print(test)
#and (df['tech_id'] == "").any() == True


df = df[df.tech_id==""]
list = []

for i in id_list:
    test = df[df['_id'] == i]
    print(test['_id'])
    

    

