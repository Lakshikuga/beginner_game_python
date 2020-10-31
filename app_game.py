print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello ", name, "you are ", age, "years old")
health = 10
if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ")
    if wants_to_play.lower() == "yes":
        print("You are starting with ", str(health),  "health")
        print("Let's play!")

        first_choice = input("First Choice... Left or Right (left/right)? ")
        if first_choice.lower() == "left":
            second_choice = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")
            if second_choice.lower() == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5
                third_choice = input("You notice a house and a river. Which do you go to (river/house)? ")
                if third_choice.lower() == "river":
                    print("You fell in the river and lost 5 health")
                else:
                    print("You go to the house and are greeted by the owner... He "
                          "doesn't like you and you lose 5 health")
                health -= 5
                #he used health check here because to say that you lose or win is not because of entering the house but because your health reduced to 0.

            elif second_choice.lower() == "around":
                print("Congrats! You went around and reached the other side of the lake!")
                health += 5
                third_choice = input("Would you jump and take the rope to get to the other side of the mountain or Would you take a parachute (rope/parachute)? ")
                if third_choice.lower() == "rope":
                    print("Good! you reached on the other side of the mountain! You earned 10 health.")
                    health += 10
                else:
                    print("oops! The parachute went out of air and you fell in to the sea! you lost 15 health.")
                    health -= 15
        else:
            print("You fell down and lost...")
            health -= 10

        if health <= 0:
            print("Sorry! You now have 0 health and you lost the game...")
        else:
            print("You have survived... You have earned", health, "health and you win!")
    else:
        print("Try another day!")
else:
    print("You are too young to play!")



