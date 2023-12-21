
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[10:83+1].lower()

    for length in range(37, 60+1):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1]:
                palindromes.add(sub)

    return palindromes
