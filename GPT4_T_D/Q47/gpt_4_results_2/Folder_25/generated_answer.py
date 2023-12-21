
def palindromes_of_specific_lengths(string):
    string = string[26:85].lower()

    palindromes = set()
    
    for i in range(len(string)):
        for j in range(i+30, min(i+47, len(string)+1)):
            segment = string[i:j]
            segment_alphabet_only = "".join(ch for ch in segment if ch.isalpha())
            if segment_alphabet_only == segment_alphabet_only[::-1] and len(segment_alphabet_only) == len(segment):
                palindromes.add(segment)
    return palindromes
