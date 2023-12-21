
def palindromes_of_specific_lengths(string):
    string = string[17:73].lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+50, min(i+52, len(string)+1)):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
