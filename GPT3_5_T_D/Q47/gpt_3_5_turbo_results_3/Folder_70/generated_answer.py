
def palindromes_of_specific_lengths(string):
    substring = string[10:71]
    palindromes = set()
    for length in range(24, 53):
        for i in range(len(substring) - length + 1):
            substring_palin = substring[i:i+length].lower()
            if substring_palin == substring_palin[::-1] and substring_palin.isalpha():
                palindromes.add(substring_palin)
    return palindromes
