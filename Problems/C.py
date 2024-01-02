def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_numbers(m, n):
    primes = []
    for num in range(m, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    primes = generate_prime_numbers(m, n)
    for prime in primes:
        print(prime)
    print()
