name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You have recently acquired an A-Catraz NFT. Now you have the power to choose your road to redmeption! Your journey begins in a dark ally, and you have to option to go left or right. Wich way would you like to go? (Left/Right)" ).lower()

if answer == "left":
    answer == input("You see the police jumping out of their car and start chasing somone, you have the opportunity to intervene and catch the criminal or jump in the police car and steal it. The choice is up to you. (Help/Steal) ").lower()

    if answer == "help":
        print("You helped the police catch the criminal. To thank you the police force are offering you to offers. A full time job to continue help them catch criminals or 1000 dollars for your efforts! (Job/Money)").lower

        if answer == "money":
            print("You choose to accept the money. You are now home in your apartment when you suddenly hear knocking on your door. You open the door and see two masked men pointing a gun to your head tellin you to give them everything you got. You now have the option to be the hero and fight back or listen to the robbers and give them everything you have, including your 1000 dollar reward. (Fight/listen) ").lower

            if answer == "figth":
                print("You choose to fight. You tried to be the hero and fight back but died in the process ").lower

                if answer == "yes":
                    print("You choose to press charges. You went to court, had Harvy specter as a lawyer and won milions. You are now retired and partying with Dan Bilizerian every day. ").lower
                elif answer == "no":
                    print("You choose no to press charges. After the robbery you suffered major trauma and lived the rest of your life in depression. ").lower
                else:
                    print("Not a valid option. You lose.")
            
            elif answer == "listen":
                print("You choose to listen. After robbing you the robbers ran out of the apartment where they where met with two officers taking their daily lunch. They got arrested and sent to jail. The police are now asking you if you would like to press charges against them? (Yes/No) ").lower

        elif answer == "job":
            print("You acceped the job. You worked in the police force for 30 years, met your wife and had three kids. You are now in retirement and lived happily ever after. GAME OVER. ").lower

        else:
            print("Not a valid option. You lose. ").lower

    elif answer == "Steal":
        print("You choose to steal the police vehicle. You are now in a hot pursuite with dusins of cop cars chasing you. The intense police chatter from the radio in your car is iritating you affecting your focus on driving. You have the option to keep it on or turn it of. (On/Off) ").lower
        if answer == "on":
            print("You choose to keep it on. By keeping the police radio on you could hear there every move. In front of you on the street you see a car carrier semi truck that has just onloaded all cars with the ramp still down. Making it a perfect jump to get off the small roads, on the highway and away from the police but a risky one. Do you take the risk? (Yes/No) ").lower
            if answer == "yes":
                print("You choose to take the risk. Unforutently you didnt have enough speed so you crashed and died in the incident. ").lower
            elif answer == "no":
                print("You choose not to take the risk. instead you speed up and got away. ").lower
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    print("Wrong way. You loose")

else:
    print("Not a valid option. You lose. ")

print("Thank you for playing", name)