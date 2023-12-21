
def return_n_greatest_chars(chars: str) -> list:
    return sorted(chars, reverse=True, key=lambda x: ord(x))[:35]
