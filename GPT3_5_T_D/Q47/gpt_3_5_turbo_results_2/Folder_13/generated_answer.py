
def palindromes_of_specific_lengths(string):
    palindromes = set()
    lowercase_string = string.lower()[13:96]

    for i in range(len(lowercase_string)):
        for j in range(57, 61):
            substring = lowercase_string[i:i+j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)

    return palindromes
