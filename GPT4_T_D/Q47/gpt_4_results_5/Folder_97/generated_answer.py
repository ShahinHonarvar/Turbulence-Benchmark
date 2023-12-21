
def palindromes_of_specific_lengths(string):
    string = string[28:95].lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+38, min(i+50, len(string)+1)):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
