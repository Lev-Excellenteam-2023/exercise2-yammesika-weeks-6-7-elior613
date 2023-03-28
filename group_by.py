def group_by(f, it):
    dic={}
    for i in it:
        dic.setdefault(f(i),[])
        dic[f(i)].append(i)
    return dic
print(group_by(len, ["hi", "bye", "yo", "try"]))
