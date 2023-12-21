
def palindromes_of_specific_lengths(string):
    substring = string[23:95]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i+17, i+56):
            if j <= len(substring):
                potential_palindrome = substring[i:j]
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and potential_palindrome.isalpha():
                    palindromes.add(potential_palindrome)
    return palindromes
