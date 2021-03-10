# HW1 ANSWERS

## 1.1
See files in repo.

## 1.2

`ep_len` and `eval_batch_size` are both 1000.

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