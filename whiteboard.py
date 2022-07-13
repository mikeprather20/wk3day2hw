#Remove vowels
#Write a function that will remove all vowels 
#from a given string. The function should return a string.
#Example:
#Input: ‘Joel’
#Output: ‘Jl’

def rem_vowel(str):
   vowels = ('a', 'e', 'i', 'o', 'u') 
   for x in str.lower():
       if x in vowels:
           str = str.replace(x, "")
   return str

print(rem_vowel('Joel'))


