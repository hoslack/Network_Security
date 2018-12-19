class RSA(object):
    def __init__(self, p, q, e):
        self.e = e
        self.n = p*q
        r = [(p-1)*(q-1), e]
        t = [0, 1]
        w = [0, 0]
        while r[len(r)-1] > 0:
            w[len(w):] = [int(r[len(r)-2]/r[len(r)-1])]
            r[len(r):] = [r[len(r)-2]-w[len(r)]*r[len(r)-1]]
            t[len(t):] = [t[len(t)-2]-w[len(t)]*t[len(t)-1]]
        self.d = t[len(t)-2]
        while self.d < 0:
            self.d += r[0]

    def encrypt(self, m): return pow(m, self.e, self.n)

    def decrypt(self, c): return pow(c, self.d, self.n)


P = 9151
Q = 8573
E = 101
encrypt1 = RSA(P, Q, E)

print(encrypt1.encrypt(9359754))
print(encrypt1.decrypt(58729877))
