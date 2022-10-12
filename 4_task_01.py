# Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

from decimal import Decimal


def round(num, d):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{d}"))


print(round(float(input("Enter a real number: ")), \
    float(input("set accuracy d (10^{-1} ≤ d ≤10^{-10}): "))))