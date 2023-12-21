
def palindromes_of_specific_lengths(test_string):
    from string import ascii_letters
    
    substring = test_string[63:71]
    palindrome_set = set()

    for start in range(8):  
        for length in range(4, 6): 
            if start + length <= 8:
                candidate = substring[start:start+length]
                if candidate.lower() == candidate[::-1].lower() and candidate.isascii() and candidate.isalpha():
                    palindrome_set.add(candidate)

    return palindrome_set
