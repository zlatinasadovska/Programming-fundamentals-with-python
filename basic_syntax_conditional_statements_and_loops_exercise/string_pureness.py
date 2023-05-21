n = int(input())
output = ''

for string in range(n):
    word = input()
    if any(c in word for c in ",._"):
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
