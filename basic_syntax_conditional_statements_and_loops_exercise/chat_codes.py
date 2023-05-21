n = int(input())
message = ''

for number in range(n):
    num = int(input())

    if num == 88:
        message = "Hello"
        print(f"{message}")
    if num == 86:
        message = "How are you?"
        print(f"{message}")
    if num != 86 and num < 88:
        message = "GREAT!"
        print(f"{message}")
    if num > 88:
        message = "Bye."
        print(f"{message}")
