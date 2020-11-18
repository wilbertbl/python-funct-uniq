import os
os.system('cls')

numbers = [1, 2, 3, 3, 3, 3, 4, 5]


def angka_unik(numbers):

    list_angka_unik = []

    unik = set(numbers)

    for number in unik:
        list_angka_unik.append(number)

    return list_angka_unik


if __name__ == '__main__':
    print(angka_unik(numbers))  # hasilnya nanti 1, 2, 3, 4, 5
