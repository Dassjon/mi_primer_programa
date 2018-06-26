ice_cream_input = input("do you wanna ice cream? (YES/NO):  ").upper()

if ice_cream_input == "YES":
    ice_cream = True
elif ice_cream_input == "NO":
    ice_cream = False
else:
    print("i don't know what did you say, just answer me yes or no fucker")
    input("do you wanna ice cream? (YES/NO): ").upper()
    if ice_cream_input == "YES":
        ice_cream = True
    elif ice_cream_input == "NO":
        ice_cream = False
    else:
        print("what are you saying? answer yes or no, it's very difficulty? 7n7")
    input("do you wanna ice cream? (YES/NO): ").upper()
    if ice_cream_input == "YES":
        ice_cream = True
    elif ice_cream_input == "NO":
        ice_cream = False
    else:
        print("Next Cuestion")
        ice_cream = False


money_input = input("do you have money to buy it? (YES/NO):  ").upper()
sir_ice_input = input("is the ice cream manager here? (YES/NO): ").upper()
aunt_input = input("is your aunt here? (YES/NO): ").upper()

ice_cream = ice_cream_input == "YES"
money = money_input == "YES"
aunt = aunt_input == "YES"
can_afford_it = money or aunt
sir_ice = sir_ice_input == "YES"


if ice_cream or money or aunt or can_afford_it or sir_ice:
    print("nice, what kind of ice cream do you want?")
else:
    print("pues nada")
