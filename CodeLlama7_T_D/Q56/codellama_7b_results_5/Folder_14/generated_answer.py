
def all_substring_of_size_n(s, n):
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(substring) == n and not any(c in result for c in substring):
            result.append(substring)

    return result
