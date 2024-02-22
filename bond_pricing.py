from scipy.optimize import brentq

class Bond:
    def __init__(self, price, par, T, c, freq):
        self.price = price
        self.par = par
        self.T = T
        self.c = c
        self.freq = freq
        self.coupon = (self.c * self.par) / self.freq
        self.periods = self.T * self.freq

    def ytm(self):
        tdiff = [(i+1)/self.freq for i in range(self.T * self.freq)]
        ytm_f = lambda y: sum(self.coupon / (1 + y/self.freq)**(self.freq * t) for t in tdiff) + (self.par / (1 + y/self.freq)**(self.periods)) - self.price
        return brentq(ytm_f, 0.01, 0.2)
    