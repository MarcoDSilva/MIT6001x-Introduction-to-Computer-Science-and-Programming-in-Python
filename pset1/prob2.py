#Write a program that prints the number of times the string 'bob' occurs in s

total = 0
index = 0

while index < len(s):
    if s[index] == 'b':
        if index + 1 < len(s) and index + 2 < len(s):            
            if s[index + 1] == 'o' and s[index + 2] == 'b':
                total += 1
    index += 1
        

print("Number of times bob occurs is: " +  str(total))