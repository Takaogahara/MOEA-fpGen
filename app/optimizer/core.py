from pymoo.algorithms.nsga2 import NSGA2
from pymoo.algorithms.nsga3 import NSGA3
from pymoo.algorithms.moead import MOEAD
from pymoo.algorithms.ctaea import CTAEA
from pymoo.factory import get_reference_directions
from pymoo.optimize import minimize

from app.optimizer.problem import *
from app.optimizer.utils import *


class Optimizer:

    def __init__(self, N_VAR:int, N_OBJ:int, N_CONSTR:int,
            N_GEN:int, selected_method, jsondata, outputpath:str):

        self.N_VAR = N_VAR
        self.N_OBJ = N_OBJ
        self.N_CONSTR = N_CONSTR
        self.N_GEN = N_GEN
        self.selected_method = selected_method
        self.jsondata = jsondata
        self.outputpath = outputpath

    def execute(self):

        problem = FullFP(self.N_VAR, self.N_OBJ, self.N_CONSTR, self.jsondata)

        if self.selected_method['algorithm'] == 'NSGA2':
            algorithm = NSGA2(pop_size=self.selected_method['parameters'])

        elif self.selected_method['algorithm'] == 'NSGA3':
            ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=self.selected_method['parameters'][1])
            algorithm = NSGA3(pop_size=self.selected_method['parameters'][0], ref_dirs=ref_dirs)

        elif self.selected_method['algorithm'] == 'MOEA/D':
            ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=self.selected_method['parameters'][1])
            algorithm = MOEAD(ref_dirs, n_neighbors=self.selected_method['parameters'][0], decomposition="pbi", prob_neighbor_mating=0.7, seed=1)

        elif self.selected_method['algorithm'] == 'C-TAEA':
            ref_dirs = get_reference_directions("das-dennis", 2, n_partitions=self.selected_method['parameters'])
            algorithm = CTAEA(ref_dirs, seed=1)

        result = minimize(problem, algorithm, ('n_gen', self.N_GEN), verbose=True, seed=8)

        result_int = Polish.floatToInteger(result)
        Exports.saveCSV(result_int, self.outputpath)