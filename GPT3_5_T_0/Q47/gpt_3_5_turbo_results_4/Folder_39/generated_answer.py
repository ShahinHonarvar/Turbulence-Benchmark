
def palindromes_of_specific_lengths(string):
    substring = string[31:92].lower()
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
