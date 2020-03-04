# ConditinalDeblurGAN-Pytorch

This is an implement of DeblurGAN with Pytorch.

## Prerequisites
- Python 3.7
- Pytorch, torch>=0.4.1, torchvision>=0.2.1
- To run the code, please install required packages by the following command
```
pip install -r requirements.txt
```

## Preprocess the dataset
1. Download the dataset from [Here](https://drive.google.com/file/d/18_PcNpadgxPOSaSpsUcFiTHpxNDmMtO3/view?usp=sharing). This dataset is generated by the paper "A dataset for deep image deblurring aided by inertial sensor data".
2. Put the downloaded dataset in the folder "dataset".
3. To generate names of all the train and test data, run the file "readDatasetNames.py" 
```
python readDatasetNames.py
```

## Train the model
```
python main.py --phase train --epoch 15
```

## Test the model
```
python main.py --phase test
```