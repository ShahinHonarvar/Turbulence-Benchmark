
def palindromes_of_specific_lengths(string):
    substring = string[27:96].lower()
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(substring) - length + 1):
            substringed_palindrome = substring[i: i + length]
            if substringed_palindrome.isalpha() and substringed_palindrome == substringed_palindrome[::-1]:
                palindromes.add(substringed_palindrome)
    return palindromes
