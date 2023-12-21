
def return_n_greatest_chars(s: str) -> list:
    return sorted(s, reverse=True, key=lambda c: ord(c))[:24]
