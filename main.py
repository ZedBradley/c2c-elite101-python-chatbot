from datetime import date
def calculateAge(y, m, d):
    birthdate = date(y, m, d)
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (m, d))
    if age >= 18:
        return "you are " + str(age) + " years old, which is perfect for a new account"
    else:
        return "you are " + str(age) + " years old, so you need a co-signer"


faq = ["1. What do I need to open an account?",
       "2. How old do I have to be to open an account?",
       "3. What is overdraft protection?",
       "4. What are the interest rates for savings and checking account"]
faqAnswers = ["You need two forms of id, a verification of address (bills) and if under 18 a parent co-signer.", "You must be 18 to open a personal account, but with a co-signer (member above 18) you can have an account at any age.", "Overdraft protection stops your account from overdrafting, so if a transaction would take you below $0.00, the bank pays the cost and we take $20.00 from your next deposit.", "The interest rates we offer for a checkings account is 0.07% while a savings account offers o.4%."]


print("Welcome to The Bank of Zed, we're excited you're looking to open an account!")
name = input("What's your name? ")

y = int(input("Hello " + name + ", what year were you born? (Ex. 1997) "))
m = int(input("What month? (1-12) "))
d = int(input("Finally, what day? (1-31) "))
print("It's very nice to meet you " + name + "!")
print(calculateAge(y,m,d))

def display_menu():
    print("\n **The Bank of Zed**")
    print("1: Personal Checking")
    print("2: Personal Savings")
    print("3: Custodial Checking")
    print("4: Custodial Savings")
    print("5: FAQ's")
    print("6: exit")

def user_selection():
    while(True):
        display_menu()
        number = str(input("\nEnter a number 1-6: "))
        if(number == "1"):
            print("\nLets get started on your personal checking account!")
            valid_id = input("Do you have a valid id (State issued id or license)? ")
            if(valid_id):
                print("If you have a check to deposit we can get started right away!")
            else:
                print("Come back with an id! See you soon!")
                break
        elif(number == "2"):
            print("\nLets get started on your personal savings account!")
            valid_id = input("Do you have a valid id (State issued id or license)? ")
            if(valid_id):
                print("If you have a check to deposit we can get started right away!")
            else:
                print("Come back with an id! See you soon!")
                break
        elif(number == "3"):
            print("\nLets get started on your custodial checking account!")
            valid_id = input("Do you have a valid id (State issued id or license)? ")
            if(valid_id):
                print("If you have a check to deposit we can get started right away!")
            else:
                print("Come back with an id! See you soon!")
                break

        elif(number == "4"):
            print("\nLets get started on your custodial savings account!")
            valid_id = input("Do you have a valid id (State issued id or license)? ")
            if(valid_id):
                print("If you have a check to deposit we can get started right away!")
            else:
                print("Come back with an id! See you soon!")
                break
        elif(number == "5"):
            print("Here are some frequently asked questions, choose a number to see the answer for the corresponding question.")
            for q in faq:
                print(q)
            question = input("Which answer would you like to see? (enter 1 - 5) ")
            question = int(question)
            print(faqAnswers[question - 1])


        elif(number == "6"):
            print("\nend")
            print("Thank you for chatting, see you next time!")
            break
        else:
            print("\nnot valid input, enter number 1-5")

user_selection()
