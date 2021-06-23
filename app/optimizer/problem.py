# External imports
from pymoo.model.problem import Problem
import numpy as np

# Local imports
from app.optimizer.function import Function, Constrain


class Baseline(Problem):
    """
    Baseline problem definition
    """

    def __init__(self):
        super().__init__(n_var=2,
                         n_obj=2,
                         n_constr=2,
                         xl=np.array([-2, -2]),
                         xu=np.array([2, 2]),
                         elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[0] ** 2 + x[1] ** 2
        f2 = (x[0] - 1) ** 2 + x[1] ** 2

        g1 = 2 * (x[0] - 0.1) * (x[0] - 0.9) / 0.18
        g2 = - 20 * (x[0] - 0.4) * (x[0] - 0.6) / 4.8

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]


class FullFP(Problem):
    """
    Calculate full fingerprint sequency
    """

    def __init__(self, n_var: int, n_obj: int, n_constr: int, pathtodata):
        self.data = pathtodata
        min_searchspace = list(self.data['min'][0]['active'].values())
        max_searchspace = list(self.data['max'][0]['active'].values())

        if n_var == 0:
            N_VAR = len(max_searchspace)
        else:
            N_VAR = n_var
        N_OBJ = n_obj
        N_CONSTR = n_constr

        super().__init__(n_var=N_VAR,
                         n_obj=N_OBJ,
                         n_constr=N_CONSTR,
                         xl=np.array(min_searchspace),
                         xu=np.array(max_searchspace),
                         elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):

        func = Function(self.data)
        const = Constrain(self.data)

        f1_str = func.full_sum()
        f2_str = func.full_dist()

        g1_str = const.full_sum('+', '-')  # lower or equal <=
        g2_str = const.full_sumnot('-', '+')  # greater or equal >=

        f1 = eval(f1_str)
        f2 = eval(f2_str)

        g1 = eval(g1_str)
        g2 = eval(g2_str)

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]


class FullFPVariable(Problem):
    """
    Calculate full fingerprint sequency including variance
    in fingerprint values
    """

    def __init__(self, n_var: int, n_obj: int, n_constr: int, pathtodata):
        self.data = pathtodata
        min_searchspace = list(self.data['min'][0]['active'].values())
        max_searchspace = list(self.data['max'][0]['active'].values())

        if n_var == 0:
            N_VAR = len(max_searchspace)
        else:
            N_VAR = n_var
        N_OBJ = n_obj
        N_CONSTR = n_constr

        super().__init__(n_var=N_VAR,
                         n_obj=N_OBJ,
                         n_constr=N_CONSTR,
                         xl=np.array(min_searchspace),
                         xu=np.array(max_searchspace),
                         elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):

        func = Function(self.data)
        const = Constrain(self.data)

        f1_str = func.full_sum()
        f2_str = func.full_dist_variable()

        g1_str = const.full_sum('+', '-')  # lower or equal <=
        g2_str = const.full_sumnot('-', '+')  # greater or equal >=

        f1 = eval(f1_str)
        f2 = eval(f2_str)

        g1 = eval(g1_str)
        g2 = eval(g2_str)

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]

# @ -------------------------------------------------------------------------


class NotableFP(Problem):
    """
    Calculate only notable fingerprint sequency
    """

    def __init__(self, n_var: int, n_obj: int, n_constr: int, pathtodata):
        self.data = pathtodata
        min_searchspace = self.data['notable'][0]['min']
        max_searchspace = self.data['notable'][0]['max']

        if n_var == 0:
            N_VAR = len(max_searchspace)
        else:
            N_VAR = n_var
        N_OBJ = n_obj
        N_CONSTR = n_constr

        super().__init__(n_var=N_VAR,
                         n_obj=N_OBJ,
                         n_constr=N_CONSTR,
                         xl=np.array(min_searchspace),
                         xu=np.array(max_searchspace),
                         elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):

        func = Function(self.data)
        const = Constrain(self.data)

        f1_str = func.notable_sum()
        f2_str = func.notable_dist()

        g1_str = const.notable_sum('+', '-')  # lower or equal <=
        g2_str = const.notable_sumnot('-', '+')  # greater or equal >=

        f1 = eval(f1_str)
        f2 = eval(f2_str)
        g1 = eval(g1_str)
        g2 = eval(g2_str)

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]


class EvalTest(Problem):

    def __init__(self, n_var: int, n_obj: int, n_constr: int, pathtodata):
        self.data = pathtodata
        min_searchspace = self.data['notable'][0]['min']
        max_searchspace = self.data['notable'][0]['max']

        N_VAR = n_var
        N_OBJ = n_obj
        N_CONSTR = n_constr

        super().__init__(n_var=N_VAR,
                         n_obj=N_OBJ,
                         n_constr=N_CONSTR,
                         xl=np.array(min_searchspace),
                         xu=np.array(max_searchspace),
                         elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):

        func = Function(self.data)
        const = Constrain(self.data)

        f1_str = func.notable_sum()
        f2_str = func.notable_dist()

        g1_str = const.notable_sum('+', '-')  # lower or equal <=
        g2_str = const.notable_sumnot('-', '+')  # greater or equal >=

        f1 = eval(f1_str)
        f2 = eval(f2_str)

        g1 = eval(g1_str)
        g2 = eval(g2_str)

        out["F"] = [f1, f2]
        out["G"] = [g1, g2]
