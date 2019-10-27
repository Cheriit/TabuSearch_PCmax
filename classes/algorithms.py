def list_algorithm(CPUs, processes):
    for proc in processes:
        min(CPUs, key=lambda cpu: cpu.getFreeAt()).assign(proc)