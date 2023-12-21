
def all_substring_of_size_n(s):
    sub_strings = []
    length = 92
    for i in range(len(s)-length+1):
        substring = s[i:i+length]
        if len(set(substring)) == len(substring):
            sub_strings.append(substring)
    return list(set(sub_strings))
