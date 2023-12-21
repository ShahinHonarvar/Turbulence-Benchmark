
def palindromes_of_specific_lengths(str):
    str = str.lower()
    str = str[11:97]
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 45, min(i + 53, len(str) + 1)):  
            substr = str[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
