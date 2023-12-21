
def all_substring_of_size_n(s):
    return [s[i:i+85] for i in range(len(s)-84) if len(set(s[i:i+85])) == 85]
