
def all_substring_of_size_n(s):
    output = []
    for i in range(len(s)):
        if i + 30 > len(s):
            break
        substring = s[i:i+30]
        if len(set(substring)) == len(substring):
            output.append(substring)
    return list(set(output))
