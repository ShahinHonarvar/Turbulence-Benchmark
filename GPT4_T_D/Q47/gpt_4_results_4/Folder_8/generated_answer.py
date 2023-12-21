
def palindromes_of_specific_lengths(s):
    substr = s[17:73].lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+50, min(i+52, len(substr)+1)):
            segment = substr[i:j]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes
