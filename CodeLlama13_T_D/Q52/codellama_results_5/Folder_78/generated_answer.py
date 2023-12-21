
def palindrome_of_length_n(string):
    return {s for s in re.findall(r"(?i)(.)\1{47}", string) if len(s) == 48}
