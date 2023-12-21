
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    palindrome_set = set()
    
    for l in range(9, length + 1):
        for i in range(length - l + 1):
            candidate = s[i: i + l]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindrome_set.add(candidate)
                
    return palindrome_set
