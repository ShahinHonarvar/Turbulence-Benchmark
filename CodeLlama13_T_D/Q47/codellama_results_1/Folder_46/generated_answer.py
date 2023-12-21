
def palindromes_of_specific_lengths(string):
    indices = range(11, 98)
    lengths = range(29, 63)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    
    for i in indices:
        for j in lengths:
            substr = string[i:i+j]
            if len(substr) == j and all(c.lower() in alphabet for c in substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    
    return palindromes
