
def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if i + 68 <= len(s):
            substring = s[i:i+68]
            if len(set(substring)) == len(substring):
                if substring not in res:
                    res.append(substring)
    return res
