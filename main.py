print("Welcome to The Bank of Zed, we're excited you're looking to open an account!")
name = input("What's your name? ")
age = input("Hello " + name + ", when was your birthday? ")
print("It's very nice to meet you " + name + "!")
def display_menu():
    print("\n **The Bank of Zed**")
    print("1: Personal Checking")
    print("2: Personal Savings")
    print("3: Custodial Checking")
    print("4: Custodial Savings")
    print("5: exit")

def user_selection():
    while(True):
        display_menu()
        number = str(input("\nEnter a number 1-5: "))
        if(number == "1"):
            print("\nLets get started on your personal checking account!")
            valid_id = input("Do you have a valid id (State issued id or license)? ")
            if(valid_id):
                print("nnnn")
        elif(number == "2"):
            print("\nLets get started on your personal savings account!")

        elif(number == "3"):
            print("\nLets get started on your custodial checking account!")

        elif(number == "4"):
            print("\nLets get started on your custodial savings account!")

        elif(number == "5"):
            print("\nend")
            print("Thank you for chatting, see you next time!")
            break
        else:
            print("\nnot valid input, enter number 1-5")

user_selection()
