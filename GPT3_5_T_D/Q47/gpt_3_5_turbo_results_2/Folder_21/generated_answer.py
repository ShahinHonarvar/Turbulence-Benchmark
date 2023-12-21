
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:296].lower()
    for length in range(136, 161):
        for i in range(len(substring)):
            if i + length <= len(substring):
                sub = substring[i:i+length]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    return palindromes
