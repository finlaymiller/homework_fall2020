# HW1 ANSWERS

## 1.1

See files in repo.

## 1.2

Created with `run_bc.sh`. `ep_len` and `eval_batch_size` are both 1000. All tests were run with the default network parameters

|                     | Ant     | HalfCheetah | Hopper  | Humanoid | Walker |
|---------------------|---------|-------------|---------|----------|--------|
| Eval_AverageEpLen   | 1000.0  | 1000.0      | 304.5   | 65.8     | 1000.0 |
| Eval_AverageReturn  | 4866.1  | 4057.0      | 1054.2  | 354.1    | 5434.3 |
| Eval_MaxReturn      | 4866.1  | 4057.0      | 1066.7  | 629.3    | 5434.3 |
| Eval_MinReturn      | 4866.1  | 4057.0      | 1034.1  | 269.3    | 5434.3 |
| Eval_StdReturn      | 0.0     | 0.0         | 12.2    | 87.7     | 0.0    |
| TimeSinceStart      | 4.8     | 3.2         | 3.4     | 7.4      | 4.3    |
| Train_AverageReturn | 4713.7  | 4205.8      | 3772.7  | 10344.5  | 5566.8 |
| Train_MaxReturn     | 4725.8  | 4288.8      | 3774.6  | 10365.5  | 5576.8 |
| Train_MinReturn     | 4701.5  | 4122.7      | 3770.7  | 10323.5  | 5557.6 |
| Train_StdReturn     | 12.2    | 83.0        | 1.9     | 21.0     | 9.4    |
| Training Loss       | 0.00076 | 0.00176     | 0.00295 | 0.0497   | 0.0066 |

## 1.3

Created with `run_hyperparameters.sh`. I experimented with 3 different hyperparameters: batch size, number of layers in the network, and layer size. All tests were run on the `Humanoid-v2` agent.

### Batch Size

![batch_size error](data/hyperparameters/batch_size.png)

Hard to say much with only 1 iteration of running, but we can clearly see a marked improvement in performance as batch size increases, with diminishing returns.

### Number of Layers

![n_layers error](data/hyperparameters/n_layers.png)

### Layer Size

![size error](data/hyperparameters/size.png)

## 2.2

All network parameters were left default.

### Ant-v2

![Ant-v2 DAgger](data/dagger/Ant-v2.png)

### HalfCheetah-v2

![HalfCheetah-v2 DAgger](data/dagger/HalfCheetah-v2.png)

### Hopper-v2

![Hopper-v2 DAgger](data/dagger/Hopper-v2.png)

### Humanoid-v2

![Humanoid-v2 DAgger](data/dagger/Humanoid-v2.png)

### Walker2d-v2

![Walker2d-v2 DAgger](data/dagger/Walker2d-v2.png)
