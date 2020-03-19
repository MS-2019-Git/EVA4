# -*- coding: utf-8 -*-
"""datatransformation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t8YundxpcNxQDTrE2GvRLvcEewpBJL21
"""

import torch
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets, transforms


def load():
      # Train Phase transformations
      train_transforms = transforms.Compose([
                                            #  transforms.Resize((28, 28)),
                                            #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
                                            #transforms.RandomRotation((-7.0, 7.0), fill=(1,)),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)) # The mean and std have to be sequences (e.g., tuples), therefore you should add a comma after the values. 
                                            # Note the difference between (0.1307) and (0.1307,)
                                            ])

      # Test Phase transformations
      test_transforms = transforms.Compose([
                                            #  transforms.Resize((28, 28)),
                                            #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
                                            ])
      return train_transforms , test_transforms

def dataloaders(seed, batch_size, workers,train_transforms,test_transforms):

    SEED = seed

    # CUDA?
    cuda = torch.cuda.is_available()
    print("CUDA Available?", cuda)

    # For reproducibility
    torch.manual_seed(SEED)

    if cuda:
        torch.cuda.manual_seed(SEED)

    # dataloader arguments - something you'll fetch these from cmdprmt
    dataloader_args = dict(shuffle=True, batch_size=batch_size, num_workers=workers, pin_memory=True) if cuda else dict(shuffle=True, batch_size=batch_size)

    # Dataset and creating Train/Test Split
    train = torchvision.datasets.CIFAR10('./data', train=True, download=True, transform=train_transforms)
    test = torchvision.datasets.CIFAR10('./data', train=False, download=True, transform=test_transforms)

    # train dataloader
    trainloader = torch.utils.data.DataLoader(train, **dataloader_args)

    # test dataloader
    testloader = torch.utils.data.DataLoader(test, **dataloader_args)

    classes = ('plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    return classes,trainloader, testloader