
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    possible_palindromes = set()

    for i in range(len(string) - 50):
        for j in range(i + 51, len(string) + 1):
            possible_palindrome = string[i:j]
            if possible_palindrome == possible_palindrome[::-1]:
                if possible_palindrome.isalpha():
                    possible_palindromes.add(possible_palindrome)

    return possible_palindromes
