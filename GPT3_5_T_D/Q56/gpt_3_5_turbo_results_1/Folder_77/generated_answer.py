
def all_substring_of_size_n(string):
    result = []
    n = len(string)

    for i in range(n - 143):
        substring = string[i:i+144]
        if len(set(substring)) == 144:
            result.append(substring)
    
    return result
