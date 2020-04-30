from segnet import mobilenet_segnet

model = mobilenet_segnet(2,input_height=416,input_width=416)
model.summary()

#
# from unet import mobilenet_unet
# model = mobilenet_unet(2,416,416)
# model.summary()


# from pspnet import mobilenet_pspnet
# model = mobilenet_pspnet(2,576,576)
# model.summary()


# from deeplab import Deeplabv3
# model = Deeplabv3(classes=2,OS=16)
# model.summary()


# import torch
# print(torch.cuda.is_available())

# from segnet1 import resnet50_segnet
# model = resnet50_segnet(n_classes=2,input_height=416, input_width=416)
# model.summary()






























