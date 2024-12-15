def elliptic_curve_order(G):
    p = 127
    a = -1
    b = 3
    x, y = G
    n = 1
    x_r, y_r = x, y
    while True:
        if n == 1:
            x_r, y_r = x, y
        else:
            if x_r == x and y_r == y:
                m = (3 * x_r**2 + a) * pow(2 * y_r, p-2, p) % p
            else:
                m = (y_r - y) * pow(x_r - x, p-2, p) % p
            x_r_new = (m**2 - x_r - x) % p
            y_r_new = (m * (x_r - x_r_new) - y_r) % p
            x_r, y_r = x_r_new, y_r_new

        if (x_r, y_r) == (x, -y % p):
            return n + 1

        n += 1

if __name__ == "__main__":
    G = (66, 64)
    order = elliptic_curve_order(G)
    print(f"Order of point {G} is: {order}")
