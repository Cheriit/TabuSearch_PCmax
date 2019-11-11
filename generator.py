import sys
import configparser
import random

from helpers.file import process


def main():
    if len(sys.argv) >= 4:
        processors = sys.argv[2]
        process_count = int(sys.argv[3])
        output = open(config['dataDir']+sys.argv[1], "w")
        output.write(processors + "\n")
        output.write(str(process_count) + "\n")
        if len(sys.argv) == 6:
            min_process_len = int(sys.argv[4])
            max_process_len = int(sys.argv[5])
        else:
            min_process_len = int(config['minProcessLen'])
            max_process_len = int(config['maxProcessLen'])
        for i in range(process_count):
            output.write(str(random.randint(
                min_process_len, max_process_len)) + "\n")
        output.close()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    config = config['GENERATOR']
    main()
