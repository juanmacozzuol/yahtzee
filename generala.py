import random


def check_values(string):
    for char in string:
        if int(char) > 5:
            return False
        count = string.count(char)
        if count > 1:
            return False
    return True


def roll_and_reroll():
    dice = []

    for i in range(5):
        dice.append(random.randint(1, 6))
        print(f'Dado {i + 1}: {dice[i]}')

    reroll_count = 0
    reroll = input("Ingrese los números de los dados que quiere tirar de nuevo sin espacios o 0 para mantener la tirada : ")
    while True:
        if reroll.isdigit():
            if int(reroll) != 0:
                if len(reroll) > 5:
                    reroll = input("Ingrese una cantidad válida dados:")
                else:
                    if not check_values(reroll):
                        reroll = input("Ingresó valores duplicados o incorrectos, ingrese nuevamente:")
                    else:
                        for numbers in reroll:
                            dice[int(numbers) - 1] = random.randint(1, 6)
                        for i in range(5):
                            print(f'Dado {i + 1}: {dice[i]}')
                        reroll_count = reroll_count + 1
                        if reroll_count < 2:

                            reroll = input("Ingrese los números de los dados que quiere tirar de nuevo sin espacios o 0 para mantener la tirada : ")
                        else:
                            break
            else:
                break
        else:
            reroll = input("Ingresó valores duplicados o incorrectos, ingrese nuevamente:")
    return {"dice": sorted(dice), "rerolls": reroll_count}


def continuidad(values):
    return sorted(values) == list(range(min(values), max(values)+1))


def dice_analysis(dice):
    values = {}
    for die in dice:
        values[die] = dice.count(die)
    return values


def check_results(dice, results):
    jugadas = []

    dice_data = dice_analysis(dice["dice"])
    for key, value in dice_data.items():
        if not results[str(key)]["tachada"] and not results[str(key)]["puntos"]:
            jugadas.append({key: value*key})
    if len(dice_data) == 5 and continuidad(dice_data.keys()) and not results["escalera"]["tachada"] and not results["escalera"]["puntos"]:
        if not dice["rerolls"]:
            jugadas.append({"escalera": 25})
        else:
            jugadas.append({"escalera": 20})

    for key, value in dice_data.items():
        if value == 3 and len(dice_data) == 2 and not results["full"]["tachada"] and not results["full"]["puntos"]:
            if not dice["rerolls"]:
                jugadas.append({"full": 35})
            else:
                jugadas.append({"full": 30})
        if value >= 4 and not results["poker"]["tachada"] and not results["poker"]["puntos"]:
            if not dice["rerolls"]:
                jugadas.append({"poker": 45})
            else:
                jugadas.append({"poker": 40})
        if value == 5 and not results["generala"]["tachada"] and not results["generala"]["puntos"]:
            if results["generala"]["puntos"] == 0:
                jugadas.append({"generala": 50})
            elif not results["generala_doble"]["tachada"] and not results["generala_doble"]["puntos"]:
                jugadas.append({"generala_doble": 100})

    return jugadas
