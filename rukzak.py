# вариант 6 с заражением, рюкзак 3*3
backpack = []
points = 15
inventory = [[0 for row in range(3)] for stolb in range(3)]
total = 0


items = [
    ('r', 3, 25),
    ('p', 2, 15),
    ('a', 2, 15),
    ('m', 2, 20),
    ('i', 1, 5),
    ('k', 1, 15),
    ('x', 3, 20),
    ('t', 1, 25),
    ('f', 1, 15),
    ('d', 1, 10),
    ('s', 2, 20),
    ('c', 2, 20)
]

#добавляем обязательынй антидот в рюкзак
items.sort(key=lambda k: (k[1], -k[2]))
for item in items:
    if item[0] == 'd':
        total += item[1]
        points += item[2]
        backpack.append(item[0])

for item in items:
    if total + item[1] <= 9 and item[0] != 'd':
        total += item[1]
        points += item[2]
        for i in range(item[1]):
            backpack.append(item[0])
    elif item[0] != 'd':
        points -= item[2]


i = 0
row = 0
while row < 3:
    while i < 9:
        inventory[row][0] = backpack[i]
        inventory[row][1] = backpack[i + 1]
        inventory[row][2] = backpack[i + 2]
        i += 3
        row += 1

if points > 0:
    for rows in inventory:
        print(rows)
    print('Сумма очков:', points)
