
def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring)-length+1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
