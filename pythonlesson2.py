#2.10
line = "It's a big multipleline line with many words GvR"
words = line.split()

#2.11
for word in words:
    for char in word:
        if (char!=word[len(word)-1]):
            print(char+"_", end="")
        else: print(char+" ", end="")
print()

#2.12
for word in words:
    print(word[0], end="")

print()

for word in words:
    print(word[len(word)-1], end="")

print()

#2.13
length = sum(len(word) for word in words)
print(length)

#2.14
print(max(len(word) for word in words))

#2.15
L = ['1', '23', '456']
print("".join(element for element in L))

#2.16
newline = line.replace("GvR", "Guido van Rossum")

#2.17
print()
sort_alph = sorted(words)
for word in sort_alph:
    print(word)

print()

sort_len = sorted(words, key=len)
for word in sort_len:
    print(word) 

#2.18
big_int = 1023003200
big_str = str(big_int)
big_str.count('0')

#2.19
newL = []
for number in L:
    str_number = str(number)
    str_number_with_zeros = str_number.zfill(3)
    newL.append(str_number_with_zeros)

for number in newL:
    print(number)