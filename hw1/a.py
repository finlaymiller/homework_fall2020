import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    values = {
        'batch_size': [ 1, 100, 1000, 10000, 100000 ],
        'size': [ 16, 32, 64, 128, 256 ],
        'n_layers': [ 1, 2, 3, 4, 5 ]
    }
    for hp in ['batch_size', 'n_layers', 'size']:
        file = os.path.join(os.getcwd(), f"data/hyperparameters/{hp}.csv")
        with open(file, 'r') as f:
            print(f"Loading from file {file}")
            df = pd.read_csv(f)
            plt.figure(1)
            plt.errorbar(values[hp], df['Eval_AverageReturn'], yerr=df['Eval_StdReturn'], fmt='o')
            if hp == 'batch_size':
                plt.xscale('log')
            plt.title(f"Eval_AverageReturn vs {hp} on Humanoid-v2")
            plt.xlabel(hp)
            plt.ylabel('Eval_AverageReturn')
            plt.grid()
            plt.savefig(f'data/hyperparameters/{hp}.png')
            plt.close()

if __name__ == "__main__":
    main()
