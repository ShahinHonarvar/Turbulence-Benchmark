
def palindromes_of_specific_lengths(string):
    substring = string[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            sub_lower = sub.lower()
            if sub_lower == sub_lower[::-1] and sub_lower.isalpha():
                palindromes.add(sub)
    return palindromes
