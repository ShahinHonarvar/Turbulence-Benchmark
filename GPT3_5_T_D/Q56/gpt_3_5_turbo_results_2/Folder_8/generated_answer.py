
def all_substring_of_size_n(string):
    return [string[i:i+30] for i in range(len(string)-29) if len(set(string[i:i+30])) == 30]
