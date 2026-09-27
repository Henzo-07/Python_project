def verification():
    try:
        print("=" * 30)
        print("\t VOTER'S VERIFICATION")
        print("=" * 30)
        
        AGE = int(input("Supply your Age: "))
        if AGE <=17:
            print("Sorry you are not eligible to voter")
            return
        else:
            print("You're eligibile to Voter.")
            return
    except Exception as e:
        print("Error message:{%s}" % e)
    
first_phase = verification()
first_phase