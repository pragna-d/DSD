# //@what is pangram? it is a string where we a-z alphabets 
# str="A quick brown fox jumps over the lazy dog "
str=input("enter the alphabet: ")
alpha="abcdefghijklmnopqrstuvwxyz"
var = True
for char in alpha:
    if char not in str.lower():
        var=False
if(var==True):
    print('pangram')
        # print("not pangram")
else:
    print("not pangram")
        
        
# input
# var""
# if i not in input 