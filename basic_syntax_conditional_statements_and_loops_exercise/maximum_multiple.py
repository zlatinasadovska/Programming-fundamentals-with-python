divisor = int(input())
boundary = int(input())

maximum_multiple = 0

for number in range(1, boundary + 1):
    if number % divisor == 0:
        maximum_multiple = number

print(f"{maximum_multiple}")
