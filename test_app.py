import app

def test_add_numbers():
    assert app.add_numbers(2, 3) == 5
    assert app.add_numbers(-1, 1) == 0
    assert app.add_numbers(0, 0) == 0

def test_multiply_numbers():
    assert app.multiply_numbers(2, 3) == 6
    assert app.multiply_numbers(-1, 5) == -5
    assert app.multiply_numbers(0, 10) == 0

if __name__ == "__main__":
    test_add_numbers()
    test_multiply_numbers()
    print("Все тесты прошли успешно!")
