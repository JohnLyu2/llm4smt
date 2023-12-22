import os
import threading
import subprocess
import shlex
import time
from pathlib import Path
import csv

SOLVER_NAME = "Z3"
SOLVER_CMD = "z3 -- "
INSTANCE_DIR = "/home/z52lu/fastsmtData/smt_data/sage2/all"
TIMEOUT = 3
BATCH_SIZE = 15
RES_DIR = "/home/z52lu/llm4smt/data"

class SolverRunner(threading.Thread):
    def __init__(self, solver_name, solver_cmd, instance):
        threading.Thread.__init__(self)
        self.solver_name = solver_name
        self.solver_cmd = solver_cmd
        self.instance = instance # instance path

    def run(self):
        self.time_before = time.time()
        s_cmd = f"{self.solver_cmd} {self.instance}"
        self.p = subprocess.Popen(shlex.split(s_cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.p.wait()
        self.time_after = time.time()
    
    def collect(self):
        if self.is_alive():
            try:
                self.p.terminate()
                self.join()
            except OSError:
                pass
            return self.instance, self.solver_name, None, None
        out, err = self.p.communicate()
        out = out.decode("utf-8").strip()
        return self.instance, self.solver_name, out, self.time_after - self.time_before
    
def solver_run(solver_name, solver_cmd, benchmark_dir, timeout, batch_size, result_dir):
    sorted_instances = sorted(str(instance) for instance in Path(benchmark_dir).rglob("*.smt2"))
    instance_size = len(sorted_instances)
    res_path = os.path.join(result_dir, f"{solver_name}_{timeout}.csv")
    with open(res_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["instance", "solver", "result", "time"])
        for i in range(0, instance_size, batch_size):
            batch_instances = sorted_instances[i : min(i+batch_size, instance_size)]
            runners = []
            for instance in batch_instances:
                runners.append(SolverRunner(solver_name, solver_cmd, instance))
            for runner in runners:
                runner.start()
            time_start = time.time()
            for runner in runners:
                time_left = max(0, timeout - (time.time() - time_start))
                runner.join(time_left)
            for runner in runners:
                writer.writerow(runner.collect())

def main():
    solver_run(SOLVER_NAME, SOLVER_CMD, INSTANCE_DIR, TIMEOUT, BATCH_SIZE, RES_DIR)

if __name__ == "__main__":
    main()
