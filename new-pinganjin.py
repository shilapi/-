import json
f = open("ci.json",encoding='utf-8')
jsonin = json.load(f)
def findtarget (s,head,end) :
    re = []
    if isinstance(s,list) :
        for t in range(len(s)):
            l = str(s[t])
            headnum = l.find(head) + len(head)
            endnum = l.find(end)
            re.append(l[headnum:endnum]+"平安")
    return re
result = findtarget(jsonin,"{'ci': '","', 'explanation':")
p = ','.join(result)
output = open("平安经.txt", 'w+')
print(p,file=output)
