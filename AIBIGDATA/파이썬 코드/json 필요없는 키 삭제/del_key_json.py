import json

data = 'del_tech.json'
test =[]

with open(data) as f:
    data = json.load(f)


with open("testt.json", "w") as f:
    for i in data:
        try:
            del(i['_tech_id'], i['_tactic'])
            test.append(i)
        except:
            test.append(i)
            
    json.dump(test, f, indent='\t')
            


