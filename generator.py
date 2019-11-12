import sys
import configparser
import random
from classes import CPU
from helpers.file import process


def main():
    if len(sys.argv) >= 4:
        processors = int(sys.argv[2])
        process_count = int(sys.argv[3])
        output = open(config['dataDir']+sys.argv[1], "w")
        output.write(str(processors) + "\n")
        output.write(str(process_count) + "\n")
        if len(sys.argv) == 6:
            min_process_len = int(sys.argv[4])
            max_process_len = int(sys.argv[5])
        else:
            min_process_len = int(config['minProcessLen'])
            max_process_len = int(config['maxProcessLen'])

        CPUs = []

        for i in range(processors):
            CPUs.append(CPU.CPU())

        for i in range(process_count - processors):
            CPUs[i % len(CPUs)].assign(random.randint(min_process_len, max_process_len))

        cpu_with_max_load = max(CPUs, key=lambda cpu: cpu.getFreeAt())
        cpu_with_max_load.assign(1)
        max_load = cpu_with_max_load.getFreeAt()

        for cpu in CPUs:
            if cpu.getFreeAt() < max_load:
                cpu.assign(max_load - cpu.getFreeAt())
            
            for process in cpu.getProcesses():
                output.write(str(process) + "\n")

        CPU.drawChart(CPUs)
        output.close()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['GENERATOR']
    main()
