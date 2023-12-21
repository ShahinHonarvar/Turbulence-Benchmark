
def all_substring_of_size_n(input_string):
    substrings = set()
    n = 22

    for i in range(len(input_string) - n + 1):
        substr = input_string[i:i+n]
        if len(set(substr)) == n:
            substrings.add(substr)
            
    return list(substrings)
