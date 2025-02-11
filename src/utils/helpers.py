def validate_positive_integer(value, name):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} должен быть положительным целым числом")
