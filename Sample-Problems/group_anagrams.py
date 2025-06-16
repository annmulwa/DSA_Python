from collections import defaultdict
def groupAnagrams(strs):
    res=defaultdict(list)
    for s in strs:
        sorted_str = ''.join(sorted(s))
        res[sorted_str].append(s)
    return list(res.values())


strs = ["act","pots","tops","cat","stop","hat"]
result = groupAnagrams(strs)
print(result)