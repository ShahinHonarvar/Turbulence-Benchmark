
def palindrome_of_length_n(s):
    return {p for p in re.findall(r'\b[a-zA-Z]{84}\b', s, flags=re.IGNORECASE) if p == p[::-1]}
