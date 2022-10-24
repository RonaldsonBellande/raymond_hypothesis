import header_imports *

class zata(object):
    def __init__(self):
        self.Z = None
        self.gamma = 0
        self.zeta = 0

    # It is real when s = (1/2) but we will be trying to solve for other point other then 1/2
    def zata_func(self, s):
        self.Z = np.pi**(-s/2) * self.gamma(s/2) * self.zeta(s)

