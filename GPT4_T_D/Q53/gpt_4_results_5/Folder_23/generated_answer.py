
def palindrome_of_length_at_least_n(my_string):
    my_string = my_string.lower()
    palindromes = set()
    for start in range(len(my_string)):
        for end in range(start, len(my_string)):
            potential_palindrome = my_string[start:end+1]
            if len(potential_palindrome) >= 19 and potential_palindrome == potential_palindrome[::-1]:
                if potential_palindrome.isalpha():
                    palindromes.add(potential_palindrome)
    return palindromes
