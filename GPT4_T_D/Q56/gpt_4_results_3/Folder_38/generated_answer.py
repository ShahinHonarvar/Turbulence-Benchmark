
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string)-34):
        substr = input_string[i:i+35]
        if len(substr) == len(set(substr)):
            substrings.add(substr)
        
    return list(substrings)
