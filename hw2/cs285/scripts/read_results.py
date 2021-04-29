import os
import glob
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def get_section_results(file):
    min = []
    avg = []
    max = []
    for e in tf.compat.v1.train.summary_iterator(file):
        for v in e.summary.value:
            if v.tag == 'Eval_MinReturn':
                min.append(v.simple_value)
            elif v.tag == 'Eval_AverageReturn':
                avg.append(v.simple_value)
            if v.tag == 'Eval_MaxReturn':
                max.append(v.simple_value)
    return min, avg, max

if __name__ == '__main__':
    directory = 'data/q1a'
    data = [list(range(100))]
    allSeries = []

    for folder in os.listdir(directory):
        logdir = os.path.join(directory, folder, 'events*')
        eventfile = glob.glob(logdir)[0]

        min, avg, max = get_section_results(eventfile)
        for i, (mi, av, ma) in enumerate(zip(min, avg, max)):
            print(f"Iteration {i} | Min: {mi:.2f} | Avg: {av:.2f} | Max: {ma:.2f}")
        
        data.append([min, avg, max])
        allSeries.append(folder)

    print(f"Loaded {len(data) - 1} data from {len(allSeries)} series")

    fig, ax = plt.subplots()
    plt.title("The Effect of Advantage Standardization and Reward to Go on Large-batch Policy Gradients")
    ax.set_ylabel("Average Return")
    ax.set_xlabel("Iterations")
    for i, series in enumerate(allSeries):
        ax.plot(data[0], data[i+1][1], label=series)
        ax.fill_between(data[0], data[i+1][0], data[i+1][2], alpha=0.2)
        ax.legend()
    plt.show()
