# Coordinated Deception Game Theory
This is the repository of the Coordinated Deception Game Theory project. 


## game_model_for_honeypots.py
This program reads the strategy file (strategy-1HP-1cum) and the production ports and returns the optimal honeyport port to use.

## port_stat_extractor.py
Read the ports.txt file and generates an output with the probability distribution of each combination of ports
Usage: cat ports.txt | ./port_stat_extractor.py > ../ports-distribution.csv

## utilities_generator.py
Reads the ports.csv file and the port_attractivness.csv file and generates the utilities for the GM
