# utils/validation.py

def validate_input(prompt, type_=str, min_value=None, max_value=None):
    while True:
        value = input(prompt)
        try:
            value = type_(value)
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                raise ValueError
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
            continue
        return value