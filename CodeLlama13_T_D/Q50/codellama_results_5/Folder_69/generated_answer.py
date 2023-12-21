
def if_contains_anagrams(strs):
    return len([i for i in range(len(strs)) if strs[i].lower() == strs[i][::-1].lower() and len(strs[i]) >= 3]) >= 188
