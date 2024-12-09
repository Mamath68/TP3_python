def main():
    notes = []
    coefficients = []

    for i in range(1, 6):
        note = float(input(f"Veuillez entrer la note du module {i} : "))
        coefficient = float(input(f"Veuillez entrer le coefficient correspondant : "))
        notes.append(note)
        coefficients.append(coefficient)

    total_weighted_sum = 0
    total_coefficients = 0
    for i in range(5):
        total_weighted_sum += notes[i] * coefficients[i]
        total_coefficients += coefficients[i]

    average = total_weighted_sum / total_coefficients

    admitted = True
    for note in notes:
        if note < 8:
            admitted = False
            break

    if average <= 10:
        admitted = False

    if admitted:
        result = "L'étudiant est admis."
    else:
        result = "L'étudiant n'est pas admis."

    print(f"La moyenne générale est : {average:.2f}")
    print(result)


if __name__ == "__main__":
    main()
