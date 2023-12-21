def if_contains_anagrams(strs):
    return sum(1 for i in strs for j in strs if i == j[0].lower() for k in strs if i == k[0].lower()) >= 69
