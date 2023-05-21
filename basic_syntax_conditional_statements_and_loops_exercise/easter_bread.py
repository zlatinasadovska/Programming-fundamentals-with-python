budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_1L = flour_price_per_kg * 1.25
milk_price_needed = 0.25 * milk_price_per_1L

bread_price = flour_price_per_kg + eggs_price_per_pack + milk_price_needed

number_of_loaves = 0
colored_eggs = 0

while budget >= bread_price:

    budget -= bread_price
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
