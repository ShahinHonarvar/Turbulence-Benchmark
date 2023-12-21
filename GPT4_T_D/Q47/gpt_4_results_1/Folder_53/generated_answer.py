
def palindromes_of_specific_lengths(string):
    import re
    string = string[1:300]
    string = re.sub('[^A-Za-z]', '', string)
    string = string.lower()
    palindromes = set()

    for i in range(len(string)):
        for j in range(i+3, min(i+11, len(string)+1)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
