def find_primes_between_indices(a):
    # Insert your code here. Read input from STDIN. Print output to STDOUT
    list = []
    for i in range(19, 90):
        if i * i <= a[i] <= 1000000009:
            list.append(a[i])
    return list
