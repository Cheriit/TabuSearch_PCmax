
class PCMax():

    def __init__(self, CPUs, processes):
        self.CPUs = CPUs
        self.processes = processes

    def list(self):
        for proc in self.processes:
            min(self.CPUs, key=lambda cpu: cpu.getFreeAt()).assign(proc)
