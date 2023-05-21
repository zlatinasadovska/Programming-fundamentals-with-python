string = input()

capital_indices = [index for index in range(len(string)) if 'A' <= string[index] <= 'Z']
print(capital_indices)
