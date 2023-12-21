
def palindromes_of_specific_lengths(s):
    s = s[10:56]
    palindrome_set = set()
    for i in range(3, 8):
        for j in range(len(s)-i+1):
            candidate = s[j:j+i]
            # ensure candidate contains only english letters
            if candidate.isalpha():
                if candidate.lower() == candidate.lower()[::-1]:
                    palindrome_set.add(candidate.lower())
    return palindrome_set
