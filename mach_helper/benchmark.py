import os
import time
import warnings
from collections.abc import Iterable

from .tokenize_sexpr import SExprTokenizer
from .constructs import grammatical_construct_list
# from .config import args
from func_timeout import func_timeout, FunctionTimedOut

TIMEOUT = 5

keyword_to_index = dict((grammatical_construct_list[i], i) for i in range(
    len(grammatical_construct_list)))

class Benchmark:
    def __init__(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Could not find: {path}")
        self.path = path
        self.features = []
        self.logic = 'UNPARSED'
        self.parsed = False
        self.total_feature_time = 0.0

        self.solvers = {}
        self.scores = {}

    def get_path(self):
        return self.path

    def get_solvers(self):
        return sorted(self.solvers.values(), key=lambda p: p.get_name())

    def add_solver(self, solver, score):
        self.solvers[solver.get_name()] = solver
        self.scores[solver.get_name()] = score

    def get_score(self, solver):
        return self.scores[solver.get_name()]

    def get_logic(self): 
        return self.logic

    # Compute Features up to a timeout
    def compute_features(self):
        start = time.time()

        self.compute_core_features()

        self.total_feature_time = time.time() - start

    # John: features: occurences + is_timeout + file_size
    def compute_core_features(self):
        assert hasattr(self, 'tokens')

        self.features = [0] * (len(grammatical_construct_list) + 2)
        # benchmark file size
        self.features[-1] = float(os.path.getsize(self.path))

        def count_occurrences(sexprs, features):
            visit = sexprs[:]
            while visit:
                cur = visit.pop()
                if isinstance(cur, tuple):
                    visit.extend(cur)
                elif isinstance(cur, str):
                    if cur in keyword_to_index:
                        features[keyword_to_index[cur]] += 1
                else:
                    raise RuntimeError("parsing error")

        try:
            func_timeout(timeout=TIMEOUT,
                         func=count_occurrences,
                         args=(self.tokens, self.features))
        except FunctionTimedOut:
            warnings.warn(
                f'Timeout after {TIMEOUT} seconds of compute_core_features on {self}')
            self.features[-2] = 1
        except RecursionError:
            print(f"Recurrsion Error on :{self}")

    # Get and if necessary, compute features.
    def get_features(self):
        return self.features

    def parse(self):
        assert not hasattr(self, 'tokens')
        self.tokens = [sexpr for sexpr in SExprTokenizer(self.path)]
        self.logic = 'UNSET_LOGIC'
        for sexpr in self.tokens:
            if len(sexpr) >= 2 and sexpr[0] == 'set-logic':
                self.logic = sexpr[1]
                break
        self.compute_features()
        del self.tokens
        assert not hasattr(self, 'tokens')

    def __str__(self): 
        return f"Benchmark(self.path={self.path}, len(self.solvers)={len(self.solvers)}, self.logic={self.logic})"
    __repr__ = __str__

    def __hash__(self):
        return hash(str(self))
        
