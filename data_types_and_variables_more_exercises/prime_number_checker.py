num = int(input())

if num < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(is_prime)
