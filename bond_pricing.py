from scipy.optimize import brentq, newton

class Bond:
    def __init__(self, par, T_years, c, freq, d_held=0, T_days=0, price=None):
        self.price = price
        self.par = par
        self.c = c
        self.freq = freq
        self.d_held = d_held
        self.periods = T_years * self.freq + (T_days / 360) * self.freq
        self.coupon = (self.c / self.freq) * self.par

    def ytm(self, f_a=-0.2, f_b=0.2):
        tdiff = [(i+1)/self.freq for i in range(int(self.periods))]
        ytm_f = lambda y: sum(self.coupon / ((1 + y/self.freq)**(self.freq * (t - self.d_held))) for t in tdiff) + (self.par / (1 + y/self.freq)**(self.periods)) - self.price
        try:
            return round(brentq(ytm_f, f_a, f_b), 6)
        except ValueError:
            return newton(ytm_f, self.c/self.freq)
        
    def clean_price(self, z):
        clean_price_f = sum(self.coupon * i for i in z) + self.par * z[-1] - (self.coupon / self.freq * self.d_held / 360)
        return round(clean_price_f, 2)

        

if __name__ == "__main__":
    zs = [0.9851, 0.9851, 0.9773,  0.9695, 0.96345,  0.9574, 0.95145, 0.9455]
    
    bond = Bond(25, 2, 0.0327, 4, d_held = 61)
    print(bond.clean_price(zs)/25 * 100)
    zs = [0.992, 0.9851, 0.9773,  0.9695, 0.96345,  0.9574, 0.95145, 0.9455]
    annual_coupon_rate = 0.0327
    quarterly_coupon_rate = annual_coupon_rate / 4
    face_value = 25

    # Calculate present value of future coupon payments
    coupon_payments = sum(face_value * quarterly_coupon_rate * z for z in zs)

    # Calculate present value of face value
    face_value_pv = face_value * zs[-1]

    # Calculate bond price
    bond_price = coupon_payments + face_value_pv

    print(bond_price)