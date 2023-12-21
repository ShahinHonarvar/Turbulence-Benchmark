
def all_substring_of_size_n(string):
    return [string[i:i+58] for i in range(len(string)-57) if len(set(string[i:i+58])) == 58]
