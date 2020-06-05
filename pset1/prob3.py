#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print abc
 
#s = 'abcdefghijklmnopqrstuvwxyz'
s = 'mbntmdbkuv' #bkuv

longest_substring = ''
temp_substring = s[0]
index = 1

while index < len(s):    
    last_char = temp_substring[-1]   
    
    if last_char <= s[index]:
        temp_substring += s[index]
    else:
        if len(longest_substring) > 0:            
            if len(temp_substring) > len(longest_substring): 
                longest_substring = temp_substring
                temp_substring = s[index]    
            else:
                temp_substring = s[index]
        else:
            longest_substring = temp_substring
            temp_substring = s[index] 
        
    index += 1

if len(temp_substring) > len(longest_substring):
    longest_substring = temp_substring
    

print(f'Longest substring in alphabetical order is: {longest_substring}')