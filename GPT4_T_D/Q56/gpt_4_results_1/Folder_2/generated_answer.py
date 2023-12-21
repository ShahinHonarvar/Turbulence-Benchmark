
def all_substring_of_size_n(s):
    n = 56
    substrings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) 
                if len(s[i:j]) == n and len(set(s[i:j])) == n]
    
    return list(set(substrings))
