from game import play, reset


if __name__ == '__main__':
    while True:
        play()

        other = input("Quieres jugar otra partida? (si/no): ").lower()

        if other == "s" or other == "si":
            reset()
        else:
            break

    print("Gracias por jugar!")
