def calcular_area_rectangulo(base, altura):
    return base * altura


def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura


def main():

    base_rect = float(input("Introduce la base del rectángulo: "))
    altura_rect = float(input("Introduce la altura del rectángulo: "))
    rect_area = calcular_area_rectangulo(base_rect, altura_rect)
    print(f"Área del rectángulo: {rect_area}")


    base_triangulo = float(input("Introduce la base del triángulo: "))
    altura_triangulo = float(input("Introduce la altura del triángulo: "))
    tri_area = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print(f"Área del triángulo: {tri_area}")

if __name__ == "__main__":
    main()