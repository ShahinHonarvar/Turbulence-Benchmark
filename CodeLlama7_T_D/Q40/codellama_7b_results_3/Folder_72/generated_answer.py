
def return_n_smallest_chars(s: str) -> List[str]:
    smallest_chars = []
    for i in range(37):
        smallest_char = min(s, key=ord)
        smallest_chars.append(smallest_char)
    return sorted(smallest_chars, reverse=True)
