
def return_n_greatest_chars(chars: str) -> List[str]:
    sorted_chars = sorted(chars, reverse=True)
    return sorted_chars[:87]
