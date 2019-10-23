def process(file_path):
    file = open(file_path)
    CPUCount = int(file.readline())
    processNum = int(file.readline())
    processes = []
    for i in range(processNum):
        processes.append(int(file.readline()))
    return CPUCount, processes
