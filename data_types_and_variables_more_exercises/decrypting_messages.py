key = int(input())
n = int(input())

message = ''

for char in range(n):
    letter = input()

    number = ord(letter)
    number += key

    message += chr(number)

print(message)
