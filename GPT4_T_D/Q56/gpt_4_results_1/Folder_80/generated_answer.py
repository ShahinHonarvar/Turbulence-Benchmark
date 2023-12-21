
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        if i + 31 > len(s):
            break
        substring = s[i:i + 31]
        if len(set(list(substring))) == len(list(substring)):  
            substrings.append(substring)
    return list(set(substrings))
