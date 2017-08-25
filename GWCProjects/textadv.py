start = '''
You have two weeks off of work, so you decide to go on vacation. However, you are having trouble deciding where to go.
'''

lame_end = '''
You have an amazing, yet uneventful vacation.
'''

poor_end = '''
You have no money, no way of getting home, and you are now homeless on the windy streets of Chicago.
'''

print(start)


print("Type 'Barcelona' to go to Barcelona or 'Chicago' to go to Chicago or 'Fiji' to go to Fiji.")
location = input()
if location == "Barcelona":
    print("You're exploring the streets of Barcelona when a man approaches you. Do you want to talk or walk away?")
    print("Type 'talk' to talk to the man or 'walk away' to walk away from the man.")
    twa = input()

    if twa == "talk":
        print("The man offers you an interesting proposition: If you give him $500, you will get a superpower.")
        print("Type 'pay' to give him the $500 or 'no thank you' to decline the offer.")
        offer = input()

        if offer == "pay":
            print("Type 'fly' to be able to fly or 'read minds' to be able to read minds")
            power1 = input()

            if power1 == "fly":
                print("You go to a building's rooftop to test your new superpower and you end up jumping into a bullpen since your superpower doesn't work. You then go on to become a famous matador.")
                print("THE END")

            elif power1 == "read minds":
                print("You successfully read someone else's mind; However, because you are in Spain, their thoughts are in Spanish and you do not understand Spanish, and thus your superpower is rendered useless.")
                print("THE END")

        elif offer == "no thank you":
            print(lame_end)
            print("THE END")

    elif twa == "walk away":
        print(lame_end)
        print("THE END")

elif location == "Chicago":
    print("You're exploring the streets of Chicago when a man approaches you. Do you want to talk or walk away?")
    print("Type 'talk' to talk to the man or 'walk away' to walk away from the man.")
    twa2 = input()

    if twa2 == "talk":
        print("The man offers you an interesting proposition: If you give him $500, you will get a superpower.")
        print("Type 'pay' to give him the $500 or 'no thank you' to decline the offer.")
        offer2 = input()

        if offer2 == "pay":
            print("Type 'telekinesis' to be able to move objects with your mind or 'super strength' to be able to move anything with your pure strength.")
            power2 = input()

            if power2 == "telekinesis":
                print("You walk to a public area and challenge someone to a bet that you can lift a deep-dished pizza with your mind.")
                print("Type 'lot' to bet all of your money or 'little' to bet a quarter of your money")
                bet = input()

                if bet == "lot":
                    print("The man scammed you and you don't have a superpower; Not only did you lose $500, you also lost the rest of your remaining money.")
                    print(poor_end)
                    print("THE END")

                elif bet == 'little':
                    print("Your superpower worked and you successfully lift the pizza. You then decided to invest your money in a start-up, which makes you super rich.")
                    print("THE END")

            elif power2 == "super strength":
                print("You encounter a robber and he steals your wallet.")
                print("Type 'fight' to get your wallet back or 'flight' to let the man get away.")
                wallet = input ()

                if wallet == "fight":
                    print("You get your wallet back and then you become street crime stopper on the streets of Chicago.")
                    print("THE END")

                elif wallet == "flight":
                    print(poor_end)
                    print("THE END")

        elif offer2 == "no thank you":
            print(lame_end)
            print("THE END")

    elif twa2 == "walk away":
        print(lame_end)
        print("THE END")

elif location == "Fiji":
    print("You arrive on the island of Fiji and decide to go swimming with dolphins. Suddenly a talking dolphin swims up to up to you.")
    print("Type 'swim' to swim away from the dolphin or 'chat' to talk to the dolphin.")
    dolphin = input()

    if dolphin == "swim":
        print(lame_end)
        print("THE END")

    elif dolphin == "chat":
        print("The dolphin asks for 10 fish in exchange for giving you a superpower.")
        print("Type 'yes' or 'no'")
        choice = input()

        if choice == "yes":
            print("Type 'talk to animals' or 'shapeshift'")
            answer = input()

            if answer == "talk to animals":
                print("You are able to talk to animals, you tell your friends and family and they all think you are insane. They then proceed to leave you on the island, all alone.")
                print("THE END")

            elif answer == "shapeshift":
                print("Although you are able to shapeshift, you are only able to shapeshift into a mongoose. As such, you live the remainder of your life as a mongoose.")
                print("THE END")

        elif choice == "no":
            print(lame_end)
            print("THE END")

else:
    print("Try again!")
