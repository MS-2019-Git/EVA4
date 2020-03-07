

1) Accuracy 81% in 10 Epochs.
2) Parameters: 330,944
3) Used Depthwise Seperable Convolution, Dilated Convolution in convolution Bloack4


Model: 
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 32, 32, 32]             864
              ReLU-2           [-1, 32, 32, 32]               0
       BatchNorm2d-3           [-1, 32, 32, 32]              64
            Conv2d-4           [-1, 64, 32, 32]          18,432
              ReLU-5           [-1, 64, 32, 32]               0
       BatchNorm2d-6           [-1, 64, 32, 32]             128
            Conv2d-7          [-1, 128, 32, 32]          73,728
              ReLU-8          [-1, 128, 32, 32]               0
       BatchNorm2d-9          [-1, 128, 32, 32]             256
           Conv2d-10           [-1, 32, 32, 32]           4,096
        MaxPool2d-11           [-1, 32, 16, 16]               0
           Conv2d-12           [-1, 64, 16, 16]          18,432
             ReLU-13           [-1, 64, 16, 16]               0
      BatchNorm2d-14           [-1, 64, 16, 16]             128
           Conv2d-15          [-1, 128, 16, 16]          73,728
             ReLU-16          [-1, 128, 16, 16]               0
      BatchNorm2d-17          [-1, 128, 16, 16]             256
           Conv2d-18           [-1, 32, 16, 16]           4,096
        MaxPool2d-19             [-1, 32, 8, 8]               0
           Conv2d-20             [-1, 64, 8, 8]          18,432
             ReLU-21             [-1, 64, 8, 8]               0
      BatchNorm2d-22             [-1, 64, 8, 8]             128
           Conv2d-23            [-1, 128, 8, 8]          73,728
             ReLU-24            [-1, 128, 8, 8]               0
      BatchNorm2d-25            [-1, 128, 8, 8]             256
           Conv2d-26             [-1, 32, 8, 8]           4,096
        MaxPool2d-27             [-1, 32, 4, 4]               0
           Conv2d-28             [-1, 32, 4, 4]             288
           Conv2d-29             [-1, 64, 4, 4]           2,048
             ReLU-30             [-1, 64, 4, 4]               0
      BatchNorm2d-31             [-1, 64, 4, 4]             128
           Conv2d-32             [-1, 64, 4, 4]          36,864
             ReLU-33             [-1, 64, 4, 4]               0
      BatchNorm2d-34             [-1, 64, 4, 4]             128
        AvgPool2d-35             [-1, 64, 1, 1]               0
           Conv2d-36             [-1, 10, 1, 1]             640
================================================================
Total params: 330,944
Trainable params: 330,944
Non-trainable params: 0
