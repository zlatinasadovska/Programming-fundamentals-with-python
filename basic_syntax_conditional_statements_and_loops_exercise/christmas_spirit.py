quantity_of_decorations = int(input())
days_left = int(input())

total_price = 0
spirit_points = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_light_price = 15

for day in range(1, days_left + 1):

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_price += ornament_set_price * quantity_of_decorations
        spirit_points += 5

    if day % 3 == 0:
        total_price += (tree_skirt_price * quantity_of_decorations) + (tree_garland_price * quantity_of_decorations)
        spirit_points += 13

    if day % 5 == 0:
        total_price += tree_light_price * quantity_of_decorations
        spirit_points += 17
        if day % 3 == 0:
            spirit_points += 30

    if day % 10 == 0:
        spirit_points -= 20
        total_price += tree_skirt_price + tree_garland_price + tree_light_price

if days_left % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {spirit_points}")
