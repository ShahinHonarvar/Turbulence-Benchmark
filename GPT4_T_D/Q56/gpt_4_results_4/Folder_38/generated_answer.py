
def all_substring_of_size_n(input_string):
    substrings = set()
    length = len(input_string)
    for i in range(length):
        if i + 35 > length:
            break
        substring = input_string[i:i+35]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
