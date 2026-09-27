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
            return
    except Exception as e:
        print("Error message:{%s}" % e)
    
first_phase = verification()
first_phase