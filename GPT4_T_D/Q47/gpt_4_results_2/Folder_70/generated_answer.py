
def palindromes_of_specific_lengths(str):
    substring = str[10:71]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i+24, min(i+53, len(substring))):
            possible_palindrome = substring[i:j]
            if possible_palindrome.lower() == possible_palindrome[::-1].lower() and possible_palindrome.isalpha():
                palindromes.add(possible_palindrome.lower())
    return palindromes
