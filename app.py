import random
import sys

def check_input_int(inputs):
    try:
        num = int(inputs)
    except ValueError:
        print("That's not a valid number")
        return False

    return True

def random_choice():
    # INPUT - HOW MANY CHOICES
    choice_count = input("How many different choices do you have?: ")

    while not check_input_int(choice_count):
        choice_count = input("How many different choices do you have?: ")

    choice_count = int(choice_count)

    choices = []

    # INPUT - USERS CHOICES
    for i in range(choice_count):
        x = input("Enter possible choice: ")

        while len(x) == 0:
            print("Entry cannot be blank, try again!")
            x = input("Enter possible choice: ")

        choices.append(x)

    # INPUT - HOW MANY TIMES TO RUN
    run_times = input("How many time would you like to run the program?: ")

    while not check_input_int(run_times):
        run_times = input("How many time would you like to run the program?: ")

    run_times = int(run_times)

    # STORE RESULTS OF EACH ITERATION FOR FINAL TALLY
    results = {c:0 for c in choices}

    # LOOP - RUN FOR X AMT OF TIME AND 
    # PRINT - PRINT RESULT
    for i in range(run_times):
        x = random.choice(choices)
        print(x)
        results[x] += 1

    final_choice = [choices[0], results[choices[0]]]

    for key, value in results.items():
        if value > final_choice[1]:
            final_choice[0] = key
            final_choice[1] = value

    print("Final Descision is do: " + final_choice[0])


random_choice()

# PROMT USER TO RUN , AGAIN, ENTER NEW , OR EXIT

whats_next = input("Enter \"1\" to run again or any other key to exit: ")

if whats_next == "1":
    random_choice()
else:
    sys.exit()