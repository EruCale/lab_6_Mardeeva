from calendar import month

#Task1
print("Перше завдання:\n")
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
test_years = [1900, 2000, 2004, 2100, 2400, 2024, 1800]
expected_results = [False, True, True, False, True, True, False]
all_correct = True
for i in range(len(test_years)):
    result = is_leap_year(test_years[i])
    if result != expected_results[i]:
        print(f"Помилка! Рік {test_years[i]} повернув {result}, а очікувалося {expected_results[i]}")
        all_correct = False
if all_correct:
    print("Усі результати правильні")
else:
    print("Є неправильні результати неправильні")

#Task2
print("Друге завдання:\n")
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return 29
    else:
        return month_days[month - 1]
print(days_in_month(2024, 2))
print(days_in_month(2023, 2))
print(days_in_month(2023, 11))

#Task3
print("Третє завдання:\n")
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None

    # Список кількості днів у місяцях (січень - грудень)
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Якщо рік високосний, лютому додаємо 1 день
    if month == 2 and is_year_leap(year):
        return 29

    return days_in_months[month - 1]


def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None

    # Підрахунок кількості днів до вказаного дня
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)

    # Додавання днів поточного місяця
    day_of_year += day

    return day_of_year


# Тестування функції
test_cases = [
    (1937, 12, 21, 355),
    (2000, 12, 31, 366),
    (2004, 1, 28, 28),
    (2005, 5, 27, 147),
    (2010, 5, 5, 125),
    (2010, 10, 10, 283),
    (2024, 10, 17, 291)
]

for year, month, day, expected in test_cases:
    result = day_of_year(year, month, day)
    if result == expected:
        print(f"day_of_year({year}, {month}, {day}) = {result} -> OK")
    else:
        print(f"day_of_year({year}, {month}, {day}) = {result} -> Failed, expected {expected}")
#Task4
print("Четверте завдання:\n")
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

#Task5
print("П'яте завдання:\n")
def liters_100km_to_miles_gallon(liters):
    miles_per_galon = 235.21 / liters
    return miles_per_galon
def miles_gallon_to_liters_100km(miles):
    liters_per_100km = 235.21 / miles
    return liters_per_100km
lpk_value = 8.5
mpg = liters_100km_to_miles_gallon(lpk_value)
print(f"{lpk_value} л/100 км дорівнює {mpg:.2f} MPG")
mpg_value = 30
lpk_value = miles_gallon_to_liters_100km(mpg_value)
print(f"{mpg_value} MPG дорівнює {lpk_value:.2f} л/100 км")

#Task6
print("Шосте завдання:\n")
def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 10, 12))

#Task7
print("Сьоме завдання:\n")
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2
print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(5, 12, 13))
print(is_a_right_triangle(1, 2, 3))