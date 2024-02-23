import bond_pricing

bond1 = bond_pricing.Bond(50*1.1544, 50, int((5.5*360+107)/360), 0.0214, 2)
print(bond1.ytm())