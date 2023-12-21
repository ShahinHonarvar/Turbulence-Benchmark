
def palindromes_of_specific_lengths(string):
    substring = string[11:88].lower()
    set_of_palindromes = set()
    
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            substring_palindrome = substring[i:i+length]
            if substring_palindrome == substring_palindrome[::-1] and substring_palindrome.isalpha():
                set_of_palindromes.add(substring_palindrome)
                
    return set_of_palindromes
