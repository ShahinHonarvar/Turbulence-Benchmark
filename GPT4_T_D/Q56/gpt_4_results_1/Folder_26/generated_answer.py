
def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 32):
        substring = s[i:i+33]
        if len(set(substring)) == len(substring):
            if substring not in result:
                result.append(substring)
    return result
