import sys
import urllib.request as request
import configparser

from classes import CPU, algorithms
from helpers.file import process

def setup():
    if len(sys.argv) == 2:
        CPUCount, processes = process(sys.argv[1])
    else:
        request.urlretrieve(config['url'],
                            config['path'])
        CPUCount, processes = process('./data/PCMaxMachowiak.txt')
    CPUs = []
    for i in range(CPUCount):
        CPUs.append(CPU.CPU())
    return CPUs, processes


def main():
    CPUs, processes = setup()
    algorithms.list_algorithm(CPUs, processes)

    for id, cpu in enumerate(CPUs):
        print('CPU nr. {} ends with {}'.format(id, cpu.getFreeAt()))
    CPU.drawChart(CPUs)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['DEFAULT']
    main()
