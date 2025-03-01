'''VGG11/13/16/19 in Pytorch.

The source code is adopted from:
https://github.com/kuangliu/pytorch-cifar
'''
import torch
import torch.nn as nn
import torchvision.models as models


cfg = {
    'VGG11': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'VGG13': [64, 64, 'M', 128, 128, 'M', 256, 256, 'M', 512, 512, 'M', 512, 512, 'M'],
    'VGG16': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],
    'VGG19': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 256, 'M', 512, 512, 512, 512, 'M', 512, 512, 512, 512, 'M'],
}


class VGG(nn.Module):
    def __init__(self, vgg_name, num_classes=10):
        super(VGG, self).__init__()
        self.features = self._make_layers(cfg[vgg_name])
        self.classifier = nn.Linear(512, num_classes)

    def forward(self, x):
        out = self.features(x)
        out = out.view(out.size(0), -1)
        out = self.classifier(out)
        return out

    def _make_layers(self, cfg):
        layers = []
        in_channels = 3
        for x in cfg:
            if x == 'M':
                layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
            else:
                layers += [nn.Conv2d(in_channels, x, kernel_size=3, padding=1),
                           nn.BatchNorm2d(x),
                           nn.ReLU(inplace=True)]
                in_channels = x
        layers += [nn.AdaptiveAvgPool2d((1, 1))]
        return nn.Sequential(*layers)


def vgg11(num_classes=100):
    if num_classes == 1000:
        return models.vgg11()
    return VGG("VGG19", num_classes=num_classes)

def vgg13(num_classes=100):
    if num_classes == 1000:
        return models.vgg13()
    return VGG("VGG19", num_classes=num_classes)

def vgg16(num_classes=100):
    if num_classes == 1000:
        return models.vgg16()
    return VGG("VGG19", num_classes=num_classes)

def vgg19(num_classes=100):
    if num_classes == 1000:
        return models.vgg19()
    return VGG("VGG19", num_classes=num_classes)
