number = int(input())

largest_number = int(''.join(sorted(str(number), reverse=True)))

print(largest_number)