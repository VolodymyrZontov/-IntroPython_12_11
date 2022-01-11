from lesson12_dz_10 import get_domains

print(__name__)

filename = "domains.txt"
filename = f"Homeworks/{filename}"
domains = get_domains(filename)[:10]
print(">>>>>>>", domains)


assert len(domains) >= 12, "Len domains less than 12"
print(domains[11])


value = input("Введи целое число, кроме нуля")
try:
    value = int(value)
    result = value ** -1
    print(result)
except ValueError:
    print("Вы ввели не целое число")
except ZeroDivisionError:
    print("Вы ввели 0")
