
def palindrome_of_length_at_least_n(s):
    s = ''.join(char for char in s if char.isalpha()).lower()
    n = len(s)
    result = set()
    for l in range(149, n + 1):
        for i in range(n - l + 1):
            substr = s[i: i + l]
            if substr == substr[::-1]:
                result.add(substr)
    return result
