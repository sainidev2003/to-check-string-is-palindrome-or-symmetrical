def symPal(string):
    if string==string[::-1]:
        print("the string is palindrome")
    else:
        print("the string is not palindrome")
    size=len(string)      
    if size%2==0:
        half=size//2
        if string[0:half]==string[half:size]:
            print("the string is symmetrical")
        else:
            print("the string is not symmeterical")    
    else:
        print("this is not symmetrical")  

a=input("enter the string to check whether it is symmeterical or palindrome")
symPal(a)

        