
def palindrome_of_length_at_least_n(string):
    length = len(string)
    if length < 56:
        return set()
    
    palindromes = set()
    for i in range(length - 49):
        substr = string[i:i + 25]
        rev_substr = ''.join(reversed(substr))
        if substr == rev_substr:
            palindromes.add(substr)
    
    return palindromes
