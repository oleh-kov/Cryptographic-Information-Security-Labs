from random import randint

# Параметри еліптичної кривої

# для тесту прикладу з КР
#a = -1
#b = 3
#p = 127
#G = (66, 64)

a = 1
b = 1
p = 23
G = (17, 20)

class EllipticCurve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def mod_inverse(self, a, m):
        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                gcd, x, y = egcd(b % a, a)
                return gcd, y - (b // a) * x, x

        a = a % m
        gcd, x, _ = egcd(a, m)
        if gcd != 1:
            return None
        return x % m

    def point_addition(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 == y2:
            if y1 == 0:
                return None  # Точка в нескінченності
            lam_numerator = (3 * x1 * x1 + self.a)
            lam_denominator = 2 * y1
            inv_denominator = self.mod_inverse(lam_denominator, self.p)
            if inv_denominator is None:
                return None  # Точка в нескінченності
            lam = (lam_numerator * inv_denominator) % self.p
        else:
            if x1 == x2:
                return None  # Точка в нескінченності
            lam_numerator = y2 - y1
            lam_denominator = x2 - x1
            inv_denominator = self.mod_inverse(lam_denominator, self.p)
            if inv_denominator is None:
                return None  # Точка в нескінченності
            lam = (lam_numerator * inv_denominator) % self.p

        x3 = (lam * lam - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p

        return (x3, y3) if self.is_on_curve((x3, y3)) else None

    def scalar_multiply(self, k, P):
        R = None
        Q = P
        k = k % self.p

        while k:
            if k & 1:
                R = self.point_addition(R, Q)
                if R is None:
                    raise ValueError("Point addition resulted in point at infinity")
            Q = self.point_addition(Q, Q)
            if Q is None:
                raise ValueError("Point doubling resulted in point at infinity")
            k >>= 1

        return R

    def point_negation(self, P):
        if P is None:
            return None
        x, y = P
        return (x, (-y) % self.p)

    def is_on_curve(self, P):
        if P is None:
            return True

        x, y = P
        left = (y * y) % self.p
        right = (x**3 + self.a * x + self.b) % self.p
        return left == right

class ElGamalECC:
    def __init__(self, curve, base_point):
        self.curve = curve
        self.G = base_point

    def generate_key_pair(self):
        private_key = randint(2, self.curve.p - 2)
        public_key = self.curve.scalar_multiply(private_key, self.G)
        return private_key, public_key

    def encrypt(self, message_point, public_key):
        # для тесту прикладу з КР
        #k = 5
        k = randint(2, self.curve.p - 2)
        C1 = self.curve.scalar_multiply(k, self.G)
        shared_secret = self.curve.scalar_multiply(k, public_key)
        C2 = self.curve.point_addition(message_point, shared_secret)
        return C1, C2

    def decrypt(self, C1, C2, private_key):
        shared_secret = self.curve.scalar_multiply(private_key, C1)
        message_point = self.curve.point_addition(C2, 
            self.curve.point_negation(shared_secret))
        return message_point

def main():
    curve = EllipticCurve(p, a, b)

    assert curve.is_on_curve(G), "Base point is not on the curve"

    elgamal = ElGamalECC(curve, G)

    alice_private, alice_public = elgamal.generate_key_pair()
    bob_private, bob_public = elgamal.generate_key_pair()

    # для тесту прикладу з КР

    # alice_private = 7
    # alice_public = elgamal.curve.scalar_multiply(alice_private, G)
    # bob_private = 7
    # bob_public = elgamal.curve.scalar_multiply(bob_private, G)

    print("Alice's Private Key:", alice_private)
    print("Alice's Public Key:", alice_public)
    print("\nBob's Private Key:", bob_private)
    print("Bob's Public Key:", bob_public)

    # для тесту прикладу з КР
    #message_point = (66, 64)

    message_point = (13, 7)

    C1, C2 = elgamal.encrypt(message_point, bob_public)
    
    print("\nCiphertext C1:", C1)
    print("Ciphertext C2:", C2)

    decrypted_point = elgamal.decrypt(C1, C2, bob_private)
    
    print("\nDecrypted Message Point:", decrypted_point)
    
    assert decrypted_point == message_point, "Decryption failed"

    print("Encryption and decryption successful!")

if __name__ == "__main__":
    main()
