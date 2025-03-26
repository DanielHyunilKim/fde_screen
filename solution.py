# units are cm or kg
MAX_DIMENSION = 150
MAX_VOLUME = 1000000
MAX_MASS = 20


def is_bulky(width, height, length) -> bool:
    width, height, length = float(width), float(height), float(length)
    volume = width * height * length
    return volume >= MAX_VOLUME or width >= MAX_DIMENSION or height >= MAX_DIMENSION or length >= MAX_DIMENSION


def is_heavy(mass) -> bool:
    return float(mass) >= MAX_MASS


def sort(width, height, length, mass) -> str:

    if not (width and height and length and mass):
        return "INVALID INPUT"

    try:
        float(width)
        float(height)
        float(length)
        float(mass)
    except ValueError:
        return "INVALID INPUT"

    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
