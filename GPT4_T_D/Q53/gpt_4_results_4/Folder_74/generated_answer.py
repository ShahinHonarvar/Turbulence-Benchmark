
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res_set = set()
    length = len(s)
    
    for start in range(length):
        for end in range(start + 57, length + 1):
            candidate = s[start:end]
            if candidate == candidate[::-1] and candidate.isalpha():
                res_set.add(candidate)

    return res_set
