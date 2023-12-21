
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[31:92].lower()
    
    for i in range(len(substring) - 53):
        for length in range(50, 54):
            potential_palindrome = substring[i:i+length]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    
    return palindromes
