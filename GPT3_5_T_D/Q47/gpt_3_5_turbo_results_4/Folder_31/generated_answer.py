
def palindromes_of_specific_lengths(string):
    substring = string[11:84]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(37, 61):
            current_palindrome = substring[i:i+j]
            if current_palindrome.lower() == current_palindrome.lower()[::-1] and current_palindrome.isalpha():
                palindromes.add(current_palindrome)
    return palindromes
