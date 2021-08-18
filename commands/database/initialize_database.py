
import json
def ini(name):
    with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)
    existname=0
    for item in range(len(data["people"])):
        if name in data["people"][item]:
            existname=1
    if existname==0:
        p={name:[{"evereat":[]},{"ranking":0},{"money":0},{"vegvolume":0},{"veg":0},{"alarm_clock":[]}]}
        data["people"].append(p)
        with open("database1.json",mode="w",encoding='utf-8') as file:
            json.dump(data,file)
'''ini(input())
with open("database1.json",mode='r',encoding='utf-8') as file:
        data=json.load(file,strict=False)
print(data)'''
