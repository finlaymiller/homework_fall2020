import os
import json
from collections import OrderedDict

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', type=str, required=True, default="1.2")    
    args = parser.parse_args()

    # convert args to dictionary
    params = vars(args)
    if (params["q"] == "1.2"):
        logs = OrderedDict()
        for filename in os.listdir(os.path.join(os.getcwd(), 'data/logs')):
            with open(os.path.join(os.path.join(os.getcwd(), 'data/logs'), filename), 'r') as f:
                print(f"Loading from file {filename}")
                for k, v in json.load(f).items():
                    print(f'{k} : {v}')
    elif (params["q"] == "1.3"):
        logs = OrderedDict()
        for filename in os.listdir(os.path.join(os.getcwd(), 'data/logs')):
            with open(os.path.join(os.path.join(os.getcwd(), 'data/logs'), filename), 'r') as f:
                print(f"Loading from file {filename}")
                for k, v in json.load(f).items():
                    print(f'{k} : {v}')

if __name__ == "__main__":
    main()
