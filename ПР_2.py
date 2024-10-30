import random


def read_number_from_file(filename):
    try:
        with open(filename, 'r') as file:
            number = int(file.read().strip())
        return number
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None
    except ValueError:
        print("Помилка при читанні числа з файлу.")
        return None


def generate_random_number():
    return random.randint(1, 100)


def main():
    file_number = read_number_from_file("input.txt")
    if file_number is None:
        return

    random_number = generate_random_number()
    print(f"Згенероване випадкове число: {random_number}")

    try:
        user_input = int(input("Введіть число, яке є сумою чисел з файлу та згенерованого числа: "))
    except ValueError:
        print("Будь ласка, введіть дійсне число.")
        return

    if user_input == file_number + random_number:
        print("Ви ввели правильне число!")
    else:
        print("Число введено неправильно.")


if __name__ == "__main__":
    main()