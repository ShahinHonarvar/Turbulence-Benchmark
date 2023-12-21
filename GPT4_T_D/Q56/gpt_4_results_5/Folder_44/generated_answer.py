
def all_substring_of_size_n(s):
    size = 90
    sub_strings = set()
    for i in range(len(s)-size+1):
        sub = s[i:i+size]
        if len(set(sub)) == size:
            sub_strings.add(sub)
    return list(sub_strings)
