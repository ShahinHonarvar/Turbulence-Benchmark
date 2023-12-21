
def palindromes_of_specific_lengths(string):
    return {p for p in set([re.sub('[^A-Za-z]+', '', string[i:j]) for i in range(3, 301) for j in range(i+29, 301) if len(re.sub('[^A-Za-z]+', '', string[i:j])) == len(p) and p == p[::-1] or not re.match('^[A-Za-z]*$', p)]])}
