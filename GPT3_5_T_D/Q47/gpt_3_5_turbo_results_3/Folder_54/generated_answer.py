
def palindromes_of_specific_lengths(string):
    substring = string[27:78]
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(i + 18, i + 20):
            if j <= len(substring):
                current_word = substring[i:j].lower()
                if current_word == current_word[::-1] and current_word.isalpha():
                    palindromes.add(current_word)
    
    return palindromes
