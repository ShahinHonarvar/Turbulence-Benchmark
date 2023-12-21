
def palindrome_of_length_n(string):
    set_palindromes = set()
    for i in range(len(string) - 63 + 1):
        substr = string[i:i+63]
        if len(substr) != 63: break
        if substr == substr[::-1]:
            set_palindromes.add(substr)
    return set_palindromes
