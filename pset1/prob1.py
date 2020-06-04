#Write a program that counts up the number of vowels contained in the string s
vowels = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowels += 1

print("Number of vowels: " + str(vowels))