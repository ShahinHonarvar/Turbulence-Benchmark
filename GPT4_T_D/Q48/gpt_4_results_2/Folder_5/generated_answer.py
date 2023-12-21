
def return_binary_or_hexa(n):
    a, b = n[2], n[8]
    missing_numbers = set(range(a + 1, b)) - set(n[2:9])
    total_sum = sum(missing_numbers)
    if total_sum:
        return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]
    else:
        return ""
