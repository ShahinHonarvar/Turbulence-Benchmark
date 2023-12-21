def all_substring_of_size_n(s):
    return [[c for c in s[i:j+1]] for i in range(0, len(s)-80) for j in range(i+1, len(s)+1)]
