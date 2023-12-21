
def all_substring_of_size_n(s):
    output = []
    for i in range(len(s) - 23):
        substr = s[i:i+24]
        if len(set(substr)) == 24:
            output.append(substr)
    return list(set(output))
