
def palindromes_of_specific_lengths(s):
    extracted = s[14:91]   
    palindromes = set()

    for i in range(len(extracted)):
        for j in range(i+55, min(i+72, len(extracted)+1)):
            substring = extracted[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
                
    return palindromes
