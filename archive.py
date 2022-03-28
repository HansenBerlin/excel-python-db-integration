def isprime(compare):
    primefound = False
    for i in range(2, compare + 1):
        if (compare % i) == 0:
            primefound = True
    return primefound



print(isprime(29))

a = "I\'m hungry"

b = a[0:3]
print(b)

ud_str = "Enduranze"
ud_str = ud_str.replace('z', 'c')

print(ud_str)
ud_str = f'{ud_str[0:7]}c{ud_str[8:]}'

print(ud_str)

a = "Georgina Shacklton"
first, second = a.split(" ")
print(first.lower() + "." + second[0])

leet = "Freue mich auf ein spannendes Semester!"

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)

leet_alphabet = {'a': '5', 'b': '7', 'e': '3', 's': '8'}


def change_to_leet(text):
    for k, v in leet_alphabet.items():
        text = text.replace(k, v)
    return text



for x in range(400):
    if (float(f"1e{x}") == float('inf')):
        print(x)
        break
