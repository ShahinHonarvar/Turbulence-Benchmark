
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[63:71].lower()
    
    for i in range(len(substring) - 3):
        for j in range(i + 4, min(i + 6, len(substring) + 1)):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    
    return palindromes
