
def palindromes_of_specific_lengths(string):
    set_of_palindromes = set()
    substring = string[0:5]
    for l in range(3, 5):
        for i in range(len(substring)):
            if i+l <= len(substring):
                substring_cand = substring[i:i+l]
                if substring_cand.lower() == substring_cand[::-1].lower() and substring_cand.isalpha():
                    set_of_palindromes.add(substring_cand)
    return set_of_palindromes
