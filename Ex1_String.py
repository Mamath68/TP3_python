def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.upper()}"


def main():
    people = []
    for _ in range(2):
        last_name = str(input("Entrez le nom : "))
        first_name = str(input("Entrez le prénom : "))
        people.append((last_name, first_name))

    # Trie par nom, puis par prénom en cas de noms identiques
    people.sort(key=lambda x: (x[0].lower(), x[1].lower()))

    for last_name, first_name in people:
        print(format_name(first_name, last_name))


if __name__ == "__main__":
    main()
