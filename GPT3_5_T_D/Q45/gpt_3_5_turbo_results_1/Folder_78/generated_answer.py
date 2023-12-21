
def palindromes_between_indices(string):
    letters = [c.lower() for c in string[6:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i+2, len(letters)+1):
            substring = "".join(letters[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
