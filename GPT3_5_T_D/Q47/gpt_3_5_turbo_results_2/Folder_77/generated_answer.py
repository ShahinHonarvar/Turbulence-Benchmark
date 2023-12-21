
def palindromes_of_specific_lengths(string):
    substring = string[103:277]
    palindromes = set()
    for length in range(100, 170):
        for i in range(len(substring) - length):
            sub = substring[i:i+length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
