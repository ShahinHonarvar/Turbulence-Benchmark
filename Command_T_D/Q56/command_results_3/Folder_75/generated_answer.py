def all_substring_of_size_n(s):
    return [c for c in range(1,len(s)+1) if all(x==y for x,y in zip(s[:c],s[c:]))]
