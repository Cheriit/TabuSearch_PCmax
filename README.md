# Requirements:
* python 3
* virtualenv
# Instalation:
```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
# Configuration:
File `config.ini` is a configuration file with the parameters like:
* generations - maximum number of generations
* tabu_len - maximum lenght of tabu list. This value have to be matched to an instance
* divider - paremeter defining percentage of cpu's to generate possible options
# Running script:
## Running single instance
```
python main.py $file_name
```
Where $file_name is an file name inside of directory “/data”
## Running all instances
```
./start.sh
```
This script will run all instances inside `/data` directory. However you should always match good parameters to an instance. 

# Example paramteres:
In file `instances_results.txt` is a list with all parameters and recieved results
