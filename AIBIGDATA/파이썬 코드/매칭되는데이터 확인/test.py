import pandas as pd

with open("test.txt") as f:
    data = f.readlines()

id_list = []
for line in data:
    line = line.strip()
    id_list.append(line)

print(len(id_list))
#pd.set_option('display.max_columns', None)
df = pd.read_json("fix3.json")


#attack_id = df['_id'] == 'b0303d74-3883-4e91-b4fa-4fefe6b2a21c'
#df = df[attack_id]

cnt = 0

for i in id_list:
    if (df['_id'] == i).any() == True:
        cnt += 1
    
print(cnt)

    #attack_id = df['_id'] == i
    #test = df[attack_id]
#print(test)

    #print(test)


