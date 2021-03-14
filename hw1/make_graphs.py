import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', type=str, required=True, default="batch_size")    
    args = parser.parse_args()
    params = vars(args)

    fig_folder = f"data/figs/{params['v']}"
    make_log_graph = False

    if params['v'] == 'batch_size':
        make_log_graph = True
        values = [ 1, 100, 1000, 10000, 100000 ]
    elif params['v'] == 'size':
        values = [ 16, 32, 64, 128, 256 ]
    elif params['v'] == 'n_layers':
        values = [ 1, 2, 3, 4, 5 ]

    os.makedirs(fig_folder)
    for filename in os.listdir(os.path.join(os.getcwd(), 'data/logs')):
        with open(os.path.join(os.path.join(os.getcwd(), 'data/logs'), filename), 'r') as f:
            print(f"Loading from file {filename}")
            df = pd.read_csv(f)
            df[params['v']] = values
            for column in df:
                plt.figure(1)
                if make_log_graph:
                    plt.subplot(211)

                plt.plot(df[params['v']], df[column])
                plt.xlabel(params['v'])
                plt.ylabel(column)
                plt.grid()
                
                if make_log_graph:
                    plt.subplot(212)
                    plt.loglog(df[params['v']], df[column])
                    plt.xlabel(params['v'])
                    plt.ylabel(column)
                    plt.grid()
                plt.savefig(f'{fig_folder}/{column}.png')
                plt.close()

if __name__ == "__main__":
    main()
