
def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)-13):
        substring = s[i:i+14]
        if len(set(substring)) == 14:
            result.add(substring)
    return list(result)
