
def return_n_greatest_chars(chars: str) -> List[str]:
    return sorted(chars, reverse=True, key=lambda x: ord(x))[:37]
