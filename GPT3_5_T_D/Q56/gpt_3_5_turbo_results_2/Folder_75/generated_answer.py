
def all_substring_of_size_n(string):
    return [string[i:i+16] for i in range(len(string)-15) if len(set(string[i:i+16])) == 16]
