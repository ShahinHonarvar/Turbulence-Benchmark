
def palindromes_of_specific_lengths(string):
    string = string[1:9].lower()
    palindromes = set()

    for i in range(len(string)):
        for j in range(i+3, min(i+5, len(string)+1)):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)

    return palindromes
