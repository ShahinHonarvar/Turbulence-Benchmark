
def palindrome_of_length_n(string, n):
    if len(string) < 2*n:
        return set()
    
    result = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr == substr[::-1]:
            result.add(substr)
    
    return result
