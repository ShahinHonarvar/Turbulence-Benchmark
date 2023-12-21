def identical_elements(a, b):
    return set(a[:7] + b[:7] + a[7:-7] + b[7:-7])
