
def all_substring_of_size_n(string):
    substrings = []
    length = 57
    for i in range(len(string)-length+1):
        substring = string[i:i+length]
        if len(set(substring)) == length:
            substrings.append(substring)
    return substrings
