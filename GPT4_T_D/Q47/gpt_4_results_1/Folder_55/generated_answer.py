
def palindromes_of_specific_lengths(string):
    substr = string[10:76].lower()
    substr_length = len(substr)
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(10, 21):
        for index in range(substr_length - length + 1):
            potential_palindrome = substr[index:index+length]
            if set(potential_palindrome).issubset(valid_chars) and potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes
