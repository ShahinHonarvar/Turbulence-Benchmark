
def all_substring_of_size_n(string):
    substrings = set()
    length = 117
    for i in range(len(string)):
        if i + length > len(string):
            break
        elif len(set(string[i:i+length])) == length:
            substrings.add(string[i:i+length])
    return list(substrings)
