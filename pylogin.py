# print a title on the console
print("Please login here".center(100))

# Take userName & Password from user and store into a variable.
# to take input use "input()" method.

userName = input("enter user Name:\t").strip()
passsword = input("enter password:\t").strip()

#logic
# if user entered userName and password matches
# display login successful
if userName == "kumar" and passsword == "kumar143@":
    print("login successful")
# disaply invalid error message
#now display error messages individually i.e.,
else:
    # if both userName & password wrong display:- "invalid userName and password".
    if userName != "kumar" and passsword != "kumar143@":
        print("invalid userName and password")
    # if userName wrong display:-"invalid userName"
    elif userName != "kumar":
        print("invalid userName")
    # if password wrong display:-"invalid password"
    elif passsword != "kumar143@":
        print("invalid password")


