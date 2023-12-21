
def palindrome_of_length_n(s):
    return {p for p in re.findall(r"(?i)(.)\1{398}", s) if len(p) == 401}
