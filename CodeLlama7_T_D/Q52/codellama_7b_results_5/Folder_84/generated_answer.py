
def palindrome_of_length_n(string):
    # Find all substrings of the given string
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) == 131:
                substrings.append(substring)
    # Check if any of the substrings are palindromes
    palindromes = []
    for substring in substrings:
        is_palindrome = True
        for i in range(len(substring)):
            if substring[i] != substring[-i-1]:
                is_palindrome = False
                break

        if is_palindrome:
            palindromes.append(substring)

    return set(palindromes)
