
def all_substring_of_size_n(s):
    return [''.join(sorted(s[i:i+50])) for i in range(len(s)-49)]
