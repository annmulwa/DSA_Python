def isAnagram(s, t):
    if (sorted(s) == sorted(t)):
        return True
    return False



s = "raceca"
t = "carrace"
result = isAnagram(s, t)
print(result)