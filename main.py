import generala
from string import ascii_uppercase


def main():
    vueltas = 0
    results = {
        "1": {"puntos": 0, "tachada": False},
        "2": {"puntos": 0, "tachada": False},
        "3": {"puntos": 0, "tachada": False},
        "4": {"puntos": 0, "tachada": False},
        "5": {"puntos": 0, "tachada": False},
        "6": {"puntos": 0, "tachada": False},
        "escalera": {"puntos": 0, "tachada": False},
        "full": {"puntos": 0, "tachada": False},
        "poker": {"puntos": 0, "tachada": False},
        "generala": {"puntos": 0, "tachada": False},
        "generala_doble": {"puntos": 0, "tachada": False}
    }

    puntaje = 0
    while vueltas < 11:
        dice = generala.roll_and_reroll()
        possible_plays = (generala.check_results(dice, results))
        posibles = []

        print("Seleccione una posible jugada:")

        for result in results:
            for ind, play in enumerate(possible_plays):
                for key, value in play.items():
                    if result == str(key):
                        posibles.append(ascii_uppercase[ind])
                        if type(key) == int:
                            print(f"{ascii_uppercase[ind]}.{value} puntos al {key}")
                        else:
                            print(f"{ascii_uppercase[ind]}.{key.capitalize()} por {value} puntos ")
        decision = input("Ingrese la letra correspondiente a la jugada a anotar, o el nombre de la jugada a tachar: ")
        while True:
            if decision.lower() in results.keys():
                if not results[decision.lower()]["tachada"]:
                    results[decision.lower()]["tachada"] = True
                    break
                else:
                    decision = input("Jugada ya tachada, seleccione otra: ")
            elif decision.upper() in posibles:
                key = list(possible_plays[posibles.index(decision.upper())].keys())[0]
                points = list(possible_plays[posibles.index(decision.upper())].values())[0]
                results[str(key)]["puntos"] = points
                break
            else:
                decision = input("Ingrese un valor válido: ")
        vueltas += 1

    for jugada in results.items():
        puntaje += jugada[1]["puntos"]
    print("Su puntaje es: " + str(puntaje))


main()
