Assigment 4
==============

Applying Islands technique for diversity in Evolutionary Strategies
--------------


Pre-requisites
-------------
- Python 3.x
- python-pip
- (Optional) virtualenv

How to make it work:
--------------
0. Install python dependencies
   ```
	virtualenv .venv
        source .venv/bin/activate
        pip install -r ../../requirements.txt
   ```

1. Let's play with it ...
   ```
      $ ./assigmt4.py -n 5 -g 100 -i 5 --iexchange 3 --exchange 100 --strategy es -f f2

      # output
      Generation :#100
       -> Exchange in Generation: 100
       Generation :#200
       -> Exchange in Generation: 200
      Generation :#300
       -> Exchange in Generation: 300
       Generation :#400
       -> Exchange in Generation: 400
       Generation :#500
       -> Exchange in Generation: 500
       Generation :#600
       -> Exchange in Generation: 600
       Generation :#700
       -> Exchange in Generation: 700
       Generation :#800
       -> Exchange in Generation: 800
       Generation :#900
       -> Exchange in Generation: 900
       #########################
       # Strategy              : Evolutionary Strategies
       # Generations           : 1000
       # Best Solution Value   : 19.883
       # Best Solution Fitness : 195.32
       # Obtained from  Island : 0
       # Log File              : ./es0.dat
       # Graph                 : Evolutionary_Strategies_F2.png
   ```

2. Need help in command options...?
   ```
	$ ./assigment4.py --help
	usage: assigmt4.py [-h] [-n N] [-g GENS] [--exchange EXCHANGE]
	                   [--iexchange IEXCHANGE] [-i ISLANDS] [--strategy STRATEGY]
			   [-f FITNESS]
        optional arguments:
	-h, --help            show this help message and exit
	-n N                  Population
	-g GENS, --generations GENS Number of Generations
	--exchange EXCHANGE   How often exchange populations
	--iexchange IEXCHANGE How many individual to exchange
	-i ISLANDS, --islands ISLANDS How many Parallel Islands
	--strategy STRATEGY   Strategy [ga|es]
	-f FITNESS, --fitness FITNESS Fitness Function [f2|f3|f5]

