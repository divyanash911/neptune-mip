from .utils import *

class Poseidon:
    def __init__(self):
        pass

    def init_vars(self):
        raise NotImplementedError("Solvers must implement init_vars()")
    
    def init_constraints(self):
        raise NotImplementedError("Solvers must implement init_constraints()")
    
    def init_objective(self):
        raise NotImplementedError("Solvers must implement init_objective()")
    
    def results(self):
        raise NotImplementedError("Solvers must implement results()")