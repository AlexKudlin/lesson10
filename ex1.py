pets = {}

# Добавлеям питомцев
n = int(input("Кол-во питомцев: "))

for _ in range(n):
    name = input("Введите кличку питомца: ")

    pets[name] = {
        "Вид питомца": input("Введите вид питомца: "),
        "Возраст питомца": int(input("Введите возраст питомца: ")),
        "Имя владельца": input("Введите имя владельца: ")
    }

# База питомцев
while True:
    selected_name = input("Выберите питомца (q для выхода): ")

    if selected_name.lower() == "q":
        break

    if selected_name in pets.keys():
        names = list(pets.keys())
        datas = list(pets.values())
        index = names.index(selected_name)

        age = datas[index]["Возраст питомца"]
        if age % 10 == 1 and age != 11:
            per = "год"
        elif 2 <= age % 10 <= 4 and not (12 <= age <= 14):
            per = "года"
        else:
            per = "лет"

        answer = (
            f"Это {datas[index]['Вид питомца']} по кличке '{names[index]}'. "
            f"Возраст питомца: {age} {per}. "
            f"Имя владельца: {datas[index]['Имя владельца']}"
        )

        print(answer)
    else:
        print("Такого питомца нет")