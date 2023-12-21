
def palindrome_of_length_n(s):
    return set(filter(lambda x: len(x) == 95 and all(c in string.ascii_letters for c in x), re.findall(r"(?i)(.)\1", s)))
