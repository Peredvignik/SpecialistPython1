# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

names_str=""
for name in names:
    names_str += name + ", "
print(names_str[:-2])

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
