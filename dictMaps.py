n = int(input())
phonebook = {}

for i in range(n):
    line = input()
    pair = line.split()
    phonebook[pair[0]] = pair[1]

while True:
    try:
        name = input()
    except EOFError as e:
        break
    if name not in phonebook.keys():
        print("Not found")
    else:
        print(f"{name}={phonebook[name]}")
