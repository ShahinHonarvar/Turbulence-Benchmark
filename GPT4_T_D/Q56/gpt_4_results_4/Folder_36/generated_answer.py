
def all_substring_of_size_n(string):
    result = []
    for i in range(len(string)-145):
        substring = string[i:i+146]
        if len(set(substring)) == len(substring):
            if substring not in result:
                result.append(substring)
    return result
