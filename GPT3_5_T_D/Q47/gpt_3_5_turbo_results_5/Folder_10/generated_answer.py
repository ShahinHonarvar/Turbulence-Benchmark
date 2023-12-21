
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:61]
    substring = substring.lower()
    
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            current = substring[i:i+length]
            if current == current[::-1] and current.isalpha():
                palindromes.add(current)
    
    return palindromes
