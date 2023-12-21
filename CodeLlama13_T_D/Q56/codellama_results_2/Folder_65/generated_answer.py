
def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 80 + 1):
        substring = s[i:i+81]
        if len(set(substring)) == 81 and not any(c in result for c in substring):
            result.append(substring)
    return result
