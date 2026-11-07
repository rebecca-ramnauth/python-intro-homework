
day = input("What day of the week is it? ").lower()

if day == "friday" or day == "saturday" or day == "sunday":
    time = input("Is it morning, afternoon, or evening? ").lower()

    if day == "friday":
        if time == "morning":
            print("Treat yourself to coffee!")
        elif time == "afternoon":
            print("Make plans for the weekend.")
        elif time == "evening":
            print("Relax with takeout and your favorite show.")
        else:
            print("Please enter morning, afternoon, or evening.")

    elif day == "saturday":
        if time == "morning":
            print("Let's do a morning workout!")
        elif time == "afternoon":
            print("You should get a sweet treat.")
        elif time == "evening":
            print("You should get dinner with friends.")
        else:
            print("Please enter morning, afternoon, or evening.")

    elif day == "sunday":
        if time == "morning":
            print("Let's go to mass!")
        elif time == "afternoon":
            print("You should meal prep for the new week.")
        elif time == "evening":
            print("Enjoy an early night in to recharge for the week!")
        else:
            print("Please enter morning, afternoon, or evening.")

else:
    print("Sorry, I only have suggestions for Friday, Saturday, and Sunday. Please enter one of those days.")


