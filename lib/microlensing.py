import numpy as np
import pandas as pd

# microlens object
class microlens(object):

    """microlens event"""
    
    # initialize object
    def __init__(self, **kwargs):

        """initialization, input is tE, U0, fs and t0"""
        
        self.tE = float(kwargs["tE"])
        self.U0 = float(kwargs["U0"])
        self.fs = float(kwargs["fs"])
        self.t0 = float(kwargs["t0"])

    # evaluate in given time array
    def eval(self, times):

        """Evaluate microlens event at given time array, return magnitude difference"""
        
        u = np.sqrt(self.U0**2 + ((times - self.t0)  /self.tE )**2)
        A = (u**2 + 2.) / (u * np.sqrt(u**2 + 3))
        dm = - 2.5 * np.log10(self.fs*(A - 1) + 1)

        return dm
        
# microlens family
class microlens_pars(object):

    """microlens parameter generator"""
    
    # initialize object
    def __init__(self, **kwargs):

        """initialization, input is filename"""
        
        self.parsfile = kwargs["parsfile"]

        df = pd.read_csv(self.parsfile, sep = "\s+")
        self.tEvals = np.array(df.tE)
        self.U0vals = np.array(df.U0)
        self.fsvals = np.array(df.fs)
        self.idx = np.array(range(len(self.tEvals)), dtype = int)
        

    # sample physical parameters
    def sample(self, nsamples):

        """sample physical parameters (tE, U0, fs) nsamples times"""

        selidx = np.random.choice(self.idx, size = nsamples, replace = True)

        return {'tE': self.tEvals[selidx], 'U0': self.U0vals[selidx], 'fs': self.fsvals[selidx]}
