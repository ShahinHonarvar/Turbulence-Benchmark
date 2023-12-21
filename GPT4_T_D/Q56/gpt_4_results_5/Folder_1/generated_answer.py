
def all_substring_of_size_n(s):
    length = 24
    substrings = [s[i:i+length] for i in range(len(s)-length+1)] 
    return [substring for substring in substrings if len(set(substring)) == length]
