
def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        if i+54 > len(s):
            break
        substring = s[i:i+54]
        if len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)
