
def all_substring_of_size_n(s):
    output = []
    for i in range(len(s)):
        if len(s[i:i+146]) == 146 and len(set(s[i:i+146])) == 146:
            output.append(s[i:i+146])
    return list(set(output))
