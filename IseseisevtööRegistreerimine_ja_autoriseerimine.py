def registreerimine(kasutajad):
    nimi = input("Sisesta nimi: ")
    if nimi in kasutajad:
        print("Kasutaja juba registreeritud.")
    else:
        parool = input("Sisesta parool: ")
        kasutajad[nimi] = parool
        print("Kasutaja registreeritud.")

def autoriseerimine(kasutajad):
    nimi = input("Sisesta nimi: ")
    if nimi in kasutajad:
        parool = input("Sisesta parool: ")
        if parool == kasutajad[nimi]:
            print("Kasutaja autoriseeritud.")
        else:
            print("Parool on vale.")
    else:
        print("Kasutajat ei leitud.")

def muuda_parooli(kasutajad):
    nimi = input("Sisesta nimi: ")
    if nimi in kasutajad:
        parool = input("Sisesta uus parool: ")
        kasutajad[nimi] = parool
        print("Parool edukalt muudetud.")
    else:
        print("Kasutajat ei leitud.")

def unustanud_parooli_taastamine(kasutajad):
    nimi = input("Sisesta nimi: ")
    if nimi in kasutajad:
        uus_parool = generate_parool()
        kasutajad[nimi] = uus_parool
        print("Parool taastatud: ", uus_parool)
    else:
        print("Kasutajat ei leitud.")

def generate_parool():
    import random
    import string
    def generate_random_string(length=12):
    kasutajad = string.ascii_letters + string.digits + string.punctuation
    result = ''
    
    for _ in range(length):
        result += random.choice(kasutajad)
    
    return result

  def():
    kasutajad = {}
    while True:
        print("\nValikud:")
        print("1. Registreerimine")
        print("2. Autoriseerimine")
        print("3. Nime või parooli muutmine")
        print("4. Unustanud parooli taastamine")
        print("5. Lõpetamine")

        valik = input("Valige number: ")
        if valik == "1":
            registreerimine(kasutajad)
        elif valik == "2":
            autoriseerimine(kasutajad)
        elif valik == "3":
            muuda_parooli(kasutajad)
        elif valik == "4":
            unustanud_parooli_taastamine(kasutajad)
        elif valik == "5":
            break
        else:
            print("Vale valik!")







           