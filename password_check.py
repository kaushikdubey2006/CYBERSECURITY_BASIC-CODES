# Check for Password Strength using Loops and conditional statements
 
Pass = input("Enter a strong password: ")
count=0
if len(Pass)<8:
    print("Please enter 8 digits for the password..")

else:
    for i in Pass:
        if i not in "1234567890!@#$%^&*()_]+{[:;<>,.?/}":
            count+=1
    if count==len(Pass):
        print("Please use number and special characer for password")
    
    else:
        print("Password creates successfully!!")
        if count<10:
            print("Your password is moderate, please use more characters and special characters for strong password")
        else:
            print("Your password is strong!!")

