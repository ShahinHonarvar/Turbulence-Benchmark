
def palindrome_of_length_n(string):
    # Find all substrings of length 56 in the given string
    substrs = [string[i:i+56] for i in range(len(string)-56)]
    
    # Filter out non-palindromes and non-English letters
    palindromes = []
    for substr in substrs:
        if len(substr) == 56 and all(c.isalpha() for c in substr):
            rev_substr = "".join(reversed(substr))
            if substr == rev_substr:
                palindromes.append(substr)
    
    return set(palindromes)
