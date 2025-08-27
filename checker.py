print("hey whats your good name ?")
name = input()
print("hii",name )
print("lets check you are eligible for voter id and licence or not ")

age=int(input("what is your age ??\n"))


if age>=18:
    print("you are eligible for voter id and licence ")
elif age == 17:
    print("soon you are going to get eligible ")
else:
    print("you are under age and not eligible  ")
