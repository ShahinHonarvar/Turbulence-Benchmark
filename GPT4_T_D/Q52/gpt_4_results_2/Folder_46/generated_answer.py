
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 464, len(s) + 1):
            subset = s[i:j]
            if subset == subset[::-1] and all(c.isalpha() for c in subset):
                result.add(subset)
    return result
