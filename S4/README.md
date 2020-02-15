# EVA4
colab Link: https://colab.research.google.com/drive/14fub0_XnIKy9do3Gnb5JLMAuJtoL8CsZ#scrollTo=MMWbLWO6FuHb


#Session4

1. Total no. of parameters=16,420 ( less than 20K parameters)

99.4% Accuracy in less than 20 Epochs
---------------------------------------
2. EVA4_S4_15Feb2020_1 : Achieved 98.74% at 19th Epoch  with lr=0.001, batch size=64
3. EVA4_S4_15Feb2020_2 : Achieved 99.43% at 17th Epoch with lr=0.003, batch size=64
4. EVA4_S4_15Feb2020_3 : Achieved 99.35% at 17th Epoch with lr=0.004, batch size=64
5. EVA4_S4_15Feb2020_Final : Achieved 99.42% accuracy at the 17th Epoch  with lr=0.005, batch size=64
------------------------------------------------------------------------------------------------------
6. Not used Fully connected layers
7. Used convolution2D,Relu,BN,Drop out,GAP,Softmax.

Logs from the "Final" code
-------------------------------

Epoch Number: 1
loss=0.03857186436653137 batch_id=937
100% 938/938 [00:16<00:00, 56.65it/s]
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:37: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.


Training Set: Accuracy: 57614/60000 (96.02%)


Test set: Average loss: 0.0528, Accuracy: 9825/10000 (98.25%)

Epoch Number: 2
loss=0.005901113152503967 batch_id=937
100% 938/938 [00:16<00:00, 57.79it/s]


Training Set: Accuracy: 59119/60000 (98.53%)


Test set: Average loss: 0.0379, Accuracy: 9878/10000 (98.78%)

Epoch Number: 3
loss=0.005268305540084839 batch_id=937
100% 938/938 [00:16<00:00, 59.51it/s]


Training Set: Accuracy: 59298/60000 (98.83%)


Test set: Average loss: 0.0424, Accuracy: 9862/10000 (98.62%)

Epoch Number: 4
loss=0.039324820041656494 batch_id=937
100% 938/938 [00:16<00:00, 58.15it/s]


Training Set: Accuracy: 59379/60000 (98.97%)


Test set: Average loss: 0.0351, Accuracy: 9885/10000 (98.85%)

Epoch Number: 5
loss=0.006325528025627136 batch_id=937
100% 938/938 [00:16<00:00, 58.20it/s]


Training Set: Accuracy: 59510/60000 (99.18%)


Test set: Average loss: 0.0260, Accuracy: 9924/10000 (99.24%)

Epoch Number: 6
loss=0.06258541345596313 batch_id=937
100% 938/938 [00:15<00:00, 59.05it/s]


Training Set: Accuracy: 59554/60000 (99.26%)


Test set: Average loss: 0.0347, Accuracy: 9890/10000 (98.90%)

Epoch Number: 7
loss=0.009418219327926636 batch_id=937
100% 938/938 [00:15<00:00, 58.97it/s]


Training Set: Accuracy: 59617/60000 (99.36%)


Test set: Average loss: 0.0212, Accuracy: 9924/10000 (99.24%)

Epoch Number: 8
loss=0.06767505407333374 batch_id=937
100% 938/938 [00:16<00:00, 58.31it/s]


Training Set: Accuracy: 59669/60000 (99.45%)


Test set: Average loss: 0.0222, Accuracy: 9927/10000 (99.27%)

Epoch Number: 9
loss=0.0019700825214385986 batch_id=937
100% 938/938 [00:16<00:00, 58.08it/s]


Training Set: Accuracy: 59688/60000 (99.48%)


Test set: Average loss: 0.0228, Accuracy: 9923/10000 (99.23%)

Epoch Number: 10
loss=0.004922077059745789 batch_id=937
100% 938/938 [00:15<00:00, 62.48it/s]


Training Set: Accuracy: 59722/60000 (99.54%)


Test set: Average loss: 0.0237, Accuracy: 9917/10000 (99.17%)

Epoch Number: 11
loss=0.00716283917427063 batch_id=937
100% 938/938 [00:15<00:00, 59.38it/s]


Training Set: Accuracy: 59742/60000 (99.57%)


Test set: Average loss: 0.0265, Accuracy: 9918/10000 (99.18%)

Epoch Number: 12
loss=0.0069342851638793945 batch_id=937
100% 938/938 [00:15<00:00, 63.02it/s]


Training Set: Accuracy: 59795/60000 (99.66%)


Test set: Average loss: 0.0226, Accuracy: 9929/10000 (99.29%)

Epoch Number: 13
loss=0.0015162229537963867 batch_id=937
100% 938/938 [00:15<00:00, 60.15it/s]


Training Set: Accuracy: 59803/60000 (99.67%)


Test set: Average loss: 0.0226, Accuracy: 9934/10000 (99.34%)

Epoch Number: 14
loss=0.001703709363937378 batch_id=937
100% 938/938 [00:15<00:00, 59.06it/s]


Training Set: Accuracy: 59813/60000 (99.69%)


Test set: Average loss: 0.0203, Accuracy: 9941/10000 (99.41%)

Epoch Number: 15
loss=0.005317181348800659 batch_id=937
100% 938/938 [00:15<00:00, 58.99it/s]


Training Set: Accuracy: 59841/60000 (99.73%)


Test set: Average loss: 0.0227, Accuracy: 9937/10000 (99.37%)

Epoch Number: 16
loss=0.00016623735427856445 batch_id=937
100% 938/938 [00:16<00:00, 58.51it/s]


Training Set: Accuracy: 59855/60000 (99.76%)


Test set: Average loss: 0.0236, Accuracy: 9932/10000 (99.32%)

Epoch Number: 17
loss=0.06389814615249634 batch_id=937
100% 938/938 [00:15<00:00, 59.94it/s]


Training Set: Accuracy: 59869/60000 (99.78%)


Test set: Average loss: 0.0209, Accuracy: 9942/10000 (99.42%)

Epoch Number: 18
loss=0.008014291524887085 batch_id=937
100% 938/938 [00:15<00:00, 58.27it/s]


Training Set: Accuracy: 59857/60000 (99.76%)


Test set: Average loss: 0.0262, Accuracy: 9922/10000 (99.22%)

Epoch Number: 19
loss=0.0022675693035125732 batch_id=937
100% 938/938 [00:15<00:00, 59.36it/s]


Training Set: Accuracy: 59875/60000 (99.79%)


Test set: Average loss: 0.0225, Accuracy: 9939/10000 (99.39%)
