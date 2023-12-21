 def all_substring_of_size_n(string, n):
    result = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == n and not any(c in result for c in substring):
            result.append(substring)

    return result
