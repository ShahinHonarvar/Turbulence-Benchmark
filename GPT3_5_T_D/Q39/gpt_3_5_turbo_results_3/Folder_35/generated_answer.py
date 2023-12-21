
def return_n_greatest_chars(string: str) -> list:
    return sorted(string, reverse=True)[:7]
