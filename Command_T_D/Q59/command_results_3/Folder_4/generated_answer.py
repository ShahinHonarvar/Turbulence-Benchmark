def all_left_truncatable_prime(lims):
    return sorted(list(range(2, lims[0] + 1)), key=lambda x: (x, str(x)), reverse=True)
