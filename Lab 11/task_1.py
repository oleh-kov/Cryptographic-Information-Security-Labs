def find_points_on_curve():
    points = []
    p = 23
    for x in range(p):
        for y in range(p):
            if (y**2) % p == (x**3 + x + 1) % p:
                points.append((x, y))
    return points

if __name__ == "__main__":
    points = find_points_on_curve()
    print("Точки на кривій:")
    for point in points:
        print(point)
