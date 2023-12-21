
def palindromes_of_specific_lengths(s):
    specific_substring = s[24:98]
    set_palindrome = set()

    for palindrome_length in range(10, 37):
        for i in range(len(specific_substring) - palindrome_length + 1):
            potential_palindrome = specific_substring[i:i+palindrome_length]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                set_palindrome.add(potential_palindrome.lower())
                
    return set_palindrome
