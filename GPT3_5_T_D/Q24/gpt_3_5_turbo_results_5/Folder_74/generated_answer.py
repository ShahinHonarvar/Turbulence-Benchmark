
def sum_of_divisors_in_range(n):
    def divisors(n):
        divs = []
        for i in range(1, int(n/2) + 1):
            if n % i == 0:
                divs.append(i)
        divs.append(n)
        return divs
    
    divs = divisors(n)
    sum_divs = sum(filter(lambda x: 40 <= x <= 74, divs))
    
    return sum_divs if sum_divs != 0 else 0
