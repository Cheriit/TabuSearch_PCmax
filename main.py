import sys
import urllib.request as request
import configparser
import signal

from classes import CPU, algorithms
from helpers.file import process

def signal_handler(sig, frame):
    print('Ctr+c - exit')
    sys.exit(0)

def setup():
    if len(sys.argv) == 2:
        CPUCount, processes = process(f'./data/{format(sys.argv[1])}')
    else:
        request.urlretrieve(config['url'],
                            config['dataDir']+config['defaultFilename'])
        CPUCount, processes = process(
            config['dataDir']+config['defaultFilename']
        )
    CPUs = []
    for i in range(CPUCount):
        CPUs.append(CPU.CPU(i))
    return CPUs, processes


def main():
    signal.signal(signal.SIGINT, signal_handler)
    CPUs, processes = setup()
    PCMax = algorithms.PCMax(CPUs, processes)
    solution = sum(processes)/len(CPUs)
    print(f"Solution: {solution}")
    best_eff = PCMax.tabu_search(int(tabu_param['generations']), int(tabu_param['tabu_len']), float(tabu_param['divider']))
    print(f"Found best solution with efficiency {best_eff/solution} ({best_eff}/{solution})")
    CPU.drawChart(CPUs)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    tabu_param = config['TABUSEARCH']
    config = config['DEFAULT']
    main()
