a_file = open("test.db", "r")
lines = a_file.readlines()

a_file.close()

count = 0
key = input("Enter key: ")
with open('test.db', 'r') as f:
    for line in f:
        skey = line.split("|")[0]
        if skey == key:
            break
        count += 1

del lines[count]

new_file = open("test.db", "w+")

for linee in lines:
    new_file.write(linee)
new_file.close()
