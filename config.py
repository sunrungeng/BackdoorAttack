import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

AGGR_MEAN = 'mean'
AGGR_GEO_MED = 'geom_median'
AGGR_FOOLSGOLD = 'foolsgold'
AGGR_MULTI_KRUM = 'multi_krum'
AGGR_TRIMMED_MEAN = 'trimmed_mean'
AGGR_BULYAN = 'bulyan'
MAX_UPDATE_NORM = 1000  # reject all updates larger than this amount
patience_iter = 20

TYPE_LOAN = 'loan'
TYPE_CIFAR = 'cifar'
TYPE_MNIST = 'mnist'
TYPE_TINYIMAGENET = 'tiny-imagenet-200'

ATTACK_MEAN = 'mean'
ATTACK_GEO_MED = 'geom_median'
ATTACK_FOOLSGOLD = 'foolsgold'
ATTACK_MULTI_KRUM = 'multi_krum'
ATTACK_TRIMMED_MEAN = 'trimmed_mean'
ATTACK_BULYAN = 'bulyan'