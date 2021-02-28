# -*- coding: utf-8 -*-

log_file = '../saved_models/model_mnist_Feb.09_09.14.57/log.txt'

false_posion = []
true_posion = []
with open(log_file) as f:
    line = f.readline().strip()
    while line:
        if line.startswith("___Test Target_Simple poisoned: False"):
            false_posion.append(round(float(line.split('(')[1].split('%')[0]), 2))
        elif line.startswith("___Test Target_Simple poisoned: True"):
            true_posion.append(round(float(line.split('(')[1].split('%')[0]), 2))
        line = f.readline().strip()

print(false_posion)
print(true_posion)