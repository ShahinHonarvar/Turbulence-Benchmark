
def palindromes_of_specific_lengths(s):
    import re
    def is_palindrome(subs):
        return subs == subs[::-1]
    
    substring = s[36:93]
    substring = re.sub("[^a-zA-Z]", "", substring)
    
    palindromes = set()
    for length in range(10, 36):
        for i in range(0, len(substring) - length + 1):
            test_str = substring[i : i + length]
            if is_palindrome(test_str.lower()):
                palindromes.add(test_str)
    
    return palindromes
