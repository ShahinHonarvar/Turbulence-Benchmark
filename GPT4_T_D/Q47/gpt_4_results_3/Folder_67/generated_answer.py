
def palindromes_of_specific_lengths(s):
    
    def check_palindrome(word):
        return word.lower() == word.lower()[::-1] and word.isalpha()

    substring = s[65:100]
    palindromes = set()
    
    for length in range(26, 34):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]
            if check_palindrome(word):
                palindromes.add(word)
    return palindromes
