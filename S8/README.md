Assignment 8:
-------------------
ResNet code is added to dnnmodel.ipynb file.[Source:https://github.com/kuangliu/pytorch-cifar/blob/master/models/resnet.py]

In this assignment have used ResNet18 architecture and the CrossEntropyLoss for CIFAR 10 dataset.

Total no. of parameters is fixed for ResNet18=11,173,962

The modules used in the solution file are kept at a libarary folder which are reused from assignment7.
-rw------- 1 root root  1076 Mar 14 15:12 displayimages.ipynb
-rw------- 1 root root  3320 Mar 14 15:13 datatransformation.ipynb
-rw------- 1 root root  3379 Mar 14 15:13 showimages.ipynb
-rw------- 1 root root 10701 Mar 14 15:13 dnnmodel.ipynb
drwx------ 3 root root  4096 Mar 14 15:38 data/
-rw------- 1 root root  4173 Mar 14 16:42 train_test.ipynb

Accuracy of the network on the 10000 test images: 85 %
-------------------------------------------------------------------------------------------------------------------------------

  0%|          | 0/391 [00:00<?, ?it/s]EPOCH: 0
Loss=0.8250489234924316 Batch_id=390 Accuracy=54.16: 100%|██████████| 391/391 [03:16<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0096, Accuracy: 5882/10000 (58.82%)

EPOCH: 1
Loss=0.8086473345756531 Batch_id=390 Accuracy=74.56: 100%|██████████| 391/391 [03:17<00:00,  2.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 7558/10000 (75.58%)

EPOCH: 2
Loss=0.46035805344581604 Batch_id=390 Accuracy=82.14: 100%|██████████| 391/391 [03:18<00:00,  2.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0055, Accuracy: 7665/10000 (76.65%)

EPOCH: 3
Loss=0.2550395727157593 Batch_id=390 Accuracy=87.56: 100%|██████████| 391/391 [03:17<00:00,  2.47it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0061, Accuracy: 7525/10000 (75.25%)

EPOCH: 4
Loss=0.25413766503334045 Batch_id=390 Accuracy=90.98: 100%|██████████| 391/391 [03:17<00:00,  2.49it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0056, Accuracy: 7862/10000 (78.62%)

EPOCH: 5
Loss=0.20729389786720276 Batch_id=390 Accuracy=93.94: 100%|██████████| 391/391 [03:17<00:00,  2.49it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0058, Accuracy: 7888/10000 (78.88%)

EPOCH: 6
Loss=0.10681022703647614 Batch_id=390 Accuracy=95.63: 100%|██████████| 391/391 [03:17<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0074, Accuracy: 7592/10000 (75.92%)

EPOCH: 7
Loss=0.17093925178050995 Batch_id=390 Accuracy=96.88: 100%|██████████| 391/391 [03:17<00:00,  2.51it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0069, Accuracy: 7866/10000 (78.66%)

EPOCH: 8
Loss=0.09885142743587494 Batch_id=390 Accuracy=97.66: 100%|██████████| 391/391 [03:16<00:00,  2.53it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0062, Accuracy: 7990/10000 (79.90%)

EPOCH: 9
Loss=0.24494001269340515 Batch_id=390 Accuracy=98.72: 100%|██████████| 391/391 [03:17<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0070, Accuracy: 7928/10000 (79.28%)

EPOCH: 10
Loss=0.1005135029554367 Batch_id=390 Accuracy=98.94: 100%|██████████| 391/391 [03:16<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0059, Accuracy: 8219/10000 (82.19%)

EPOCH: 11
Loss=0.04149794578552246 Batch_id=390 Accuracy=99.26: 100%|██████████| 391/391 [03:15<00:00,  2.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8322/10000 (83.22%)

EPOCH: 12
Loss=0.049018751829862595 Batch_id=390 Accuracy=99.63: 100%|██████████| 391/391 [03:15<00:00,  2.51it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8328/10000 (83.28%)

EPOCH: 13
Loss=0.003635573433712125 Batch_id=390 Accuracy=99.70: 100%|██████████| 391/391 [03:16<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0055, Accuracy: 8393/10000 (83.93%)

EPOCH: 14
Loss=0.0009382307762280107 Batch_id=390 Accuracy=99.95: 100%|██████████| 391/391 [03:15<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0050, Accuracy: 8505/10000 (85.05%)

EPOCH: 15
Loss=0.002298301551491022 Batch_id=390 Accuracy=100.00: 100%|██████████| 391/391 [03:15<00:00,  2.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0049, Accuracy: 8527/10000 (85.27%)

EPOCH: 16
Loss=0.0004310965596232563 Batch_id=390 Accuracy=100.00: 100%|██████████| 391/391 [03:15<00:00,  2.53it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0047, Accuracy: 8563/10000 (85.63%)

EPOCH: 17
Loss=0.0008945524459704757 Batch_id=390 Accuracy=100.00: 100%|██████████| 391/391 [03:14<00:00,  2.52it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0045, Accuracy: 8575/10000 (85.75%)

EPOCH: 18
Loss=0.0008685469510965049 Batch_id=390 Accuracy=100.00: 100%|██████████| 391/391 [03:15<00:00,  2.54it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0045, Accuracy: 8566/10000 (85.66%)

EPOCH: 19
Loss=0.000667011714540422 Batch_id=390 Accuracy=100.00: 100%|██████████| 391/391 [03:15<00:00,  2.54it/s]

Test set: Average loss: 0.0044, Accuracy: 8579/10000 (85.79%)
