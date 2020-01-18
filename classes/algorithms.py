from random import shuffle
from math import ceil

class PCMax():

    def __init__(self, CPUs, processes):
        self.CPUs = CPUs
        self.processes = processes

    def list(self):
        for proc in self.processes:
            min(self.CPUs, key=lambda cpu: cpu.getFreeAt()).assign(proc)

    def lpt(self):
        processes = sorted(self.processes, reverse=True)
        for proc in processes:
            min(self.CPUs, key=lambda cpu: cpu.getFreeAt()).assign(proc)

    def efficiency(self):
        return max(self.CPUs, key=lambda cpu: cpu.free_at).getFreeAt()

    def generate_neighbours(self, cpu_num):
        options = []
        for i in self.CPUs[:cpu_num]:
            for j in self.CPUs[-cpu_num:]:
                if i != j:
                    for k in i.proc:
                        options.append((i.id, j.id, k))
        filtered = list(dict.fromkeys(options))
        shuffle(filtered)
        return filtered

    def tabu_search(self, generations, tabu_limit, divider):
        self.list()
        maximum = self.efficiency()
        print(f"Generated greedy solution: {maximum}")
        
        for cpu in self.CPUs:
            cpu.clear()
        self.lpt()
        maximum = self.efficiency()
        print(f"Generated LPT solution: {maximum}")

        iterator = 0
        tabu_list = []
        cpu_num = ceil(len(self.CPUs)*divider)

        while iterator < generations:
            self.CPUs.sort(key=lambda cpu: cpu.free_at, reverse=True)
            options = self.generate_neighbours(cpu_num)
            best_option = 0

            while options[best_option] in tabu_list:
                best_option += 1
                if best_option == len(options):
                    print("All moves are at Tabu List.")
                    return maximum

            cpu_from = options[best_option][0]
            cpu_to = options[best_option][1]
            process = options[best_option][2]
            cpu_from_obj = [cpu for cpu in self.CPUs if cpu.id == cpu_from][0]
            cpu_to_obj =  [cpu for cpu in self.CPUs if cpu.id == cpu_to][0]
            cpu_from_obj.remove(process)
            cpu_to_obj.assign(process)

            efficiency = self.efficiency()
            if efficiency < maximum:
                print(f"Generated solution: {efficiency}, best solution: {maximum}")
                maximum = efficiency
            tabu_list.append((cpu_to, cpu_from, process))
            if len(tabu_list) > tabu_limit:
                del tabu_list[0]
            iterator += 1
        return maximum
