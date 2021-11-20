chr = input("Enter a character : \t")

if chr.upper()in ('A', 'E', 'I', 'O', 'U') or chr.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(chr,'is a vowel')
else:
    print(chr, 'is a consonant')