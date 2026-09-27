def generate_voterid():
    import random
    import string as str
    
def main():
    while True:
        try:
            print("\n" +"=" * 50)
            print("\t Welcome to INCE SYSTEM")
            print("=" * 50)
            print("1. >> Registration\n2. >> Confirm details\n3. >> Cast Voter\n4. >> Logout")
            response = input("Kindly selection from the following option above: ")
            if response == "1":
                print("still woring on it..")
            elif response == "2":
                print("still woring on it..")
            elif response == "3":
                print("still woring on it..")
            elif response == "4":
                print(" Thank you for using INCE System.")
                break
        except Exception as message:
            print(f"Error message: {message}")
            return

def verification():
    try:
        print("\n" +"=" * 50)
        print("\t VOTER'S VERIFICATION")
        print("=" * 50)
        
        AGE = int(input("Supply your Age: "))
        if AGE <=17:
            print("Sorry you are not eligible to voter")
            return
        else:
            print("You're eligibile to Voter. Kindly Proceed to the Next stage.")
            stage_one = main()
            stage_one
            return
    except Exception as e:
        print("Error message:{%s}" % e)
    
first_phase = verification()
first_phase