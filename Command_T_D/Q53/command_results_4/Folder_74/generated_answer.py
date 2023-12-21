def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(1, min(len(s) + 1, 100)):
        for j in range(i, min(len(s) + 1, 100)):
            if s[i - 1] == s[j - 1]:
                result.add(s[i:j])
    return result
