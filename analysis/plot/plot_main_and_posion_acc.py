# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


# # attack_mean 每轮固定4个攻击者 聚合20个 共100个 model_mnist_Feb.17_11.43.08
# y1 = [70.59, 93.11, 94.27, 96.21, 96.61, 97.13, 96.97, 96.74, 97.45, 97.21, 97.74, 97.89, 97.4, 97.81, 98.16]
# y2 = [99.16, 62.14, 99.25, 99.02, 99.07, 99.39, 99.64, 99.24, 99.63, 99.52, 99.69, 99.52, 99.83, 99.49, 99.82]
# x = range(len(y1))
# plt.plot(x, y1, color='blue', label='main acc')
# plt.plot(x, y2, color='red', label='posion acc')
# plt.legend()
# plt.show()

# mean 随机4个攻击者 聚合20个 共100个 model_mnist_Feb.17_13.18.33
# y1 = [97.09, 97.31, 97.21, 97.45, 97.58, 97.42, 97.76, 97.76, 97.81, 97.83, 97.98, 98.0, 98.16, 98.15, 98.19]
# y2 = [0.99, 1.96, 5.95, 23.08, 41.6, 68.8, 74.69, 87.34, 90.43, 92.12, 91.85, 92.22, 95.35, 95.36, 94.79]
# y3 = [70.59, 93.11, 94.27, 96.21, 96.61, 97.13, 96.97, 96.74, 97.45, 97.21, 97.74, 97.89, 97.4, 97.81, 98.16]
# y4 = [99.16, 62.14, 99.25, 99.02, 99.07, 99.39, 99.64, 99.24, 99.63, 99.52, 99.69, 99.52, 99.83, 99.49, 99.82]
# x = range(len(y1))
# plt.plot(x, y1, color='blue', label='FedAvg main', linewidth=2, linestyle=':')
# plt.plot(x, y2, color='red', label='FedAvg posion', linewidth=2, linestyle=':')
# plt.plot(x, y3, color='blue', label='FedAvg2 main', linewidth=2, linestyle='-')
# plt.plot(x, y4, color='red', label='FedAvg2 posion', linewidth=2, linestyle='-')
# plt.legend()
# plt.show()

# attack_mean 4个攻击者 分布式攻击 聚合20 共100个 model_mnist_Feb.17_19.46.02  参数 4/5
# y1 = [42.3, 93.81, 82.77, 95.24, 94.64, 95.83, 95.62, 96.35, 97.36, 97.23, 97.7, 97.97, 97.25, 97.93, 98.15]
# y2 = [83.02, 7.28, 98.41, 95.22, 99.31, 99.97, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
# x = range(len(y1))
# plt.plot(x, y1, color='blue', label='main acc')
# plt.plot(x, y2, color='red', label='posion acc')
# plt.legend()
# plt.show()

# mean 4个攻击者 分布式攻击 聚合20 共100个 model_mnist_Feb.17_19.46.02
# y1 = [97.2, 97.39, 97.49, 97.49, 97.49, 97.29, 97.81, 97.65, 97.54, 97.71, 97.85, 97.84, 97.96, 97.95, 98.08]
# y2 = [0.98, 0.84, 1.03, 1.54, 1.17, 2.9, 1.91, 8.21, 13.87, 21.71, 50.4, 56.13, 75.91, 84.81, 88.67]
# y3 = [42.3, 93.81, 82.77, 95.24, 94.64, 95.83, 95.62, 96.35, 97.36, 97.23, 97.7, 97.97, 97.25, 97.93, 98.15]
# y4 = [83.02, 7.28, 98.41, 95.22, 99.31, 99.97, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
# x = range(len(y1))
# plt.plot(x, y1, color='blue', label='FedAvg main', linewidth=2, linestyle=':')
# plt.plot(x, y2, color='red', label='FedAvg posion', linewidth=2, linestyle=':')
# plt.plot(x, y3, color='blue', label='FedAvg2 main', linewidth=2, linestyle='-')
# plt.plot(x, y4, color='red', label='FedAvg2 posion', linewidth=2, linestyle='-')
# plt.legend()
# plt.show()

# attack_mean 4个攻击者 分布式攻击 聚合20 共100个 model_mnist_Feb.17_19.46.02  参数 1/2  y1 y2为原始数据 y3 y4为本次数据
# y1 = [97.2, 97.39, 97.49, 97.49, 97.49, 97.29, 97.81, 97.65, 97.54, 97.71, 97.85, 97.84, 97.96, 97.95, 98.08]
# y2 = [0.98, 0.84, 1.03, 1.54, 1.17, 2.9, 1.91, 8.21, 13.87, 21.71, 50.4, 56.13, 75.91, 84.81, 88.67]
# y3 = [92.97, 97.06, 96.43, 97.26, 96.82, 97.38, 97.38, 96.9, 97.6, 97.61, 97.81, 97.99, 97.97, 98.06, 98.17]
# y4 = [5.35, 1.65, 5.68, 10.37, 50.54, 68.31, 93.01, 97.36, 98.49, 99.48, 99.6, 99.87, 99.97, 99.99, 100.0]
# x = range(len(y1))
# plt.plot(x, y1, color='blue', label='FedAvg main', linewidth=2, linestyle=':')
# plt.plot(x, y2, color='red', label='FedAvg posion', linewidth=2, linestyle=':')
# plt.plot(x, y3, color='blue', label='FedAvg2 main', linewidth=2, linestyle='-')
# plt.plot(x, y4, color='red', label='FedAvg2 posion', linewidth=2, linestyle='-')
# plt.legend()
# plt.show()

# geo_median 4个攻击者 聚合20个 共100个 集中式 model_mnist_Feb.17_15.47.28
# y1 = [97.56, 97.65, 97.74, 97.81, 97.72, 97.66, 97.83, 97.91, 97.82, 97.82, 97.92, 98.08, 98.16, 98.26, 98.17]
# y2 = [0.41, 0.43, 0.57, 0.67, 0.45, 0.93, 0.39, 1.29, 1.34, 1.14, 2.81, 1.72, 4.61, 5.85, 7.86]
# x = range(len(y1))
# plt.plot(x, y1, color='blue', label='main acc')
# plt.plot(x, y2, color='red', label='posion acc')
# plt.legend()
# plt.show()