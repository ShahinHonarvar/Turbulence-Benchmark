def find_original_set(s):
    return {x for x in range(1,len(s)+1) if all(s[i] <= x for i in range(len(s)))}
