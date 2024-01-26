# User input for number of pizza toppings
print('Welcome to MAMA MIA PIZZERIA')
y = str(input('What pizza would you like to order? '))
x = int(input('How many toppings do you want? '))
L = []

# Topping loop
for i in range(x):
    n = input('Choose a topping ')
    L.append(n)

print('You ordered a', y, 'pizza with', x, 'toppings')
print(*L, sep='\n')
