
def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 142):
        substring = s[i:i+143]
        if len(set(substring)) == len(substring):
            if substring not in result:
                result.append(substring)
    return result
