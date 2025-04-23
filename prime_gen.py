num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

low = min(num1, num2)
high = max(num1, num2)

is_prime = [True] * (high + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(high ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, high + 1, i):
            is_prime[j] = False
primeno = [i for i, prime in enumerate(is_prime) if prime and i >=low]

print(f"The prime number between {num1} and {num2} is: ")
print(primeno)
print(f"The total primes found: {len(primeno)}")
