
def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)-119):
        substr = s[i:i+120]
        if len(set(substr)) == len(substr):
            if substr not in result:
                result.append(substr)
    return result
