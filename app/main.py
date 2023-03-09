def hello_world():
    return 'Hello World!'


def baby_multi(a: int, b: int) -> int:
    baby_sum = 0
    try:
        for _ in range(abs(b)):
            baby_sum += abs(a)

        negative = (a < 0 or b < 0) and (a >= 0 or b >= 0)
        return 0 - baby_sum if negative else baby_sum

    except TypeError:
        return None
