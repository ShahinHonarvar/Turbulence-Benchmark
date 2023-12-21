
def palindromes_of_specific_lengths(string):
    # find all palindromes of length 10-35 in the substring from index 36 to 92
    palindromes = {pal[::-1].lower() for i in range(36, 93)
                   for j in range(i + 10, i + 36) if string[j:j+10] == string[j:j+10][::-1]
                   and len(pal) in range(10, 36)}
    return palindromes
