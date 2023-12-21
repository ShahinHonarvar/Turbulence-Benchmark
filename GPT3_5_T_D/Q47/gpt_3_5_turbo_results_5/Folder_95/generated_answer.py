
def palindromes_of_specific_lengths(string):
    substring = string[12:57]
    substring = substring.lower()

    palindromes = set()
    for i in range(len(substring) - 20 + 1):
        potential_palindrome = substring[i:i+21]
        if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(potential_palindrome)

    return palindromes
