# -*- coding: utf-8 -*-
import random

import numpy as np
import torch

l1 = torch.ones((2, 3))
l2 = torch.ones((2, 3))
l1.mul_(0.5)
print(l1)

x = range(4)
x = np.array(x)
random.shuffle(x)
print(x)

y = range(4, 4)
for i in y:
    print(i)
    print(1)
