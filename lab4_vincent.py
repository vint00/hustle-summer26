# Vincent T |Lab 4 | Green Tiger Team

# Ticket 1 
ages = [5,2,15,20,50,13]

for age in ages:
    if can_access(age):
        print("Granted")
    else:
        print("Too young")
# i predict 5,2 will get too young, and the others will be Granted.
# each time the loop runs, age will be the number inside

# Ticket 2
keep_checking = "yes"
while keep_checking == "yes":
    age = int(input("Input an age: "))
    if age >= 13:
        print("Allowed")
    else:
        print("Not allowed")
    keep_checking = input("Check another age: ")
# if the user types no on the first check, it doesnt run because it is supposed to be an int. Unless you mean the first iteration, then yes we can type in an age but it wont run another iteration.
    #A while loop allows us to do multiple flexible iterations based on user input.

# Ticket 3
while True:
    ask = input("Enter an age, or type Stop: ")
    if ask == "Stop":
        print("Exiting program")
        break
    else:
        if int(ask) >= 13:
            print("Approved")
        else:
            print("No")
#If we forgot the break statement, it would redo the ask.
# The difference between ticket 2 and this one is that ticket 2 uses a if statement to determine loop status, while this one uses break function to exit.

# Ticket 4
def can_access(age):
    if age >= 13:
        return True
    else: return False 
# whats different is that this is reusable for many things and saves time
#putting a check inside function allows it to be scalable so we don't repeat code

# Ticket 5
signups = [12,52,1,521414,214,12412,1231,312]

def signup_report(agelist):
    local 
    for s in signups:
        # im confused this one


        