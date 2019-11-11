import sys
import urllib.request as request
import configparser

from classes import CPU, algorithms
from helpers.file import process


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
        CPUs.append(CPU.CPU())
    return CPUs, processes


def main():
    CPUs, processes = setup()
    PCMax = algorithms.PCMax(CPUs, processes)
    PCMax.lpt()

    for id, cpu in enumerate(CPUs):
        print('CPU nr. {} ends with {}'.format(id+1, cpu.getFreeAt()))

    print('Max value: {}'.format(
        max(CPUs, key=lambda cpu: cpu.free_at).getFreeAt())
    )
    CPU.drawChart(CPUs)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['DEFAULT']
    main()
