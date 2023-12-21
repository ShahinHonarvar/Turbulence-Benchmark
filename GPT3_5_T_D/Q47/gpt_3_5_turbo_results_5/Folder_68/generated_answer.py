
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(51):
        for j in range(i+50, min(len(string), i+101)):
            substring = string[i:j+1]
            substring_lower = substring.lower()
            if substring_lower == substring_lower[::-1] and substring_lower.isalpha():
                palindromes.add(substring)
    return palindromes
