# Простая функция для тестирования
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    print("Привет от CI/CD!")
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"2 * 3 = {multiply_numbers(2, 3)}")
