
def palindromes_between_indices(string):
    indices = range(8, 10)
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    
    for i in indices:
        for j in range(i+2, len(string)):
            if string[i] == string[j]:
                substr = string[i:j+1]
                if substr.lower() in english_letters and len(substr) >= 3:
                    palindromes.add(substr)
    
    return palindromes
