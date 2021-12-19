import json

data = "data.json"

with open(data) as f:
    data = json.load(f)

tech_list=['_tatic', 'tactic', 'tactoc', '_tactic', 'tatic']
for num, json_data in enumerate(data):
    try:
        for tech in tech_list:
            if tech in list(json_data.keys()):
                data[num]["tactic"] = data[num].pop(tech)
        if "_tech_id" in list(json_data.keys()):
            data[num]["tech_id"] = data[num].pop("_tech_id")
    except:
        pass    

    data[num] = sorted(data[num].items())
    data[num] = dict(data[num])
with open("fix2.json", "w") as f:
    json.dump(data, f, indent='\t')
