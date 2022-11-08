import os
from PIL import Image
import random

file_train = open('train-before.txt',"w")
out = open("train.txt","w")
n=0
#path_train = '/scratch/dubo_01/liujia/Dataset/WHU-building-dataset/train_nooverlap/'
path_train = '/content/datasets/train/'
path_train_list = sorted(os.listdir(path_train+'input1/'))
random.shuffle(path_train_list)
for file_A in path_train_list:
    #path_file_A = path_train+"A/"+file_A
    path_file_A = path_train+"input1/"+file_A
    path_file_B = path_train+"input2/"+file_A
    path_file_label = path_train+"mask/"+file_A
    # img = Image.open(path_file_label)
    # if not img.getbbox():
    #     print(path_file_label)
    #     continue
    n+=1
    file_train.write(path_file_A + ' ' + path_file_B + ' ' + path_file_label + '\n')
print(n)
#path_train_another = '/scratch/dubo_01/liujia/Dataset/WHU-building-dataset/train_around_instance/'
path_train_another = '/content/datasets/train/'

path_train_list = sorted(os.listdir(path_train_another+'input1/'))
random.shuffle(path_train_list)
for file_A in path_train_list:
    path_file_A = path_train_another+"input1/"+file_A
    path_file_B = path_train_another+"input2/"+file_A
    path_file_label = path_train_another+"mask/"+file_A
    img = Image.open(path_file_label)
    if not img.getbbox():
        print(path_file_label)
        continue
    n+=1
    file_train.write(path_file_A + ' ' + path_file_B + ' ' + path_file_label + '\n')
file_train.close()
print(n)
with open('train-before.txt', "r") as f1:
    lines = f1.read().splitlines()
random.shuffle(lines)
for line in lines:
    out.write(line+'\n')
print("ok_train")

file_val = open('val.txt',"w")
#path_val = '/scratch/dubo_01/liujia/Dataset/WHU-building-dataset/test_nooverlap/'
path_val = '/content/datasets/val/'

path_val_list = sorted(os.listdir(path_val + 'input1/'))
random.shuffle(path_val_list)
for file_A in path_val_list:
    path_file_A = path_val+"input1/"+file_A
    path_file_B = path_val+"input2/"+file_A
    path_file_label = path_val+"mask/"+file_A
    # img = Image.open(path_file_label)
    # if not img.getbbox():
    #     print(path_file_label)
    #     continue
    file_val.write(path_file_A + ' ' + path_file_B + ' ' + path_file_label + '\n')
file_val.close()
print("ok_val")

file_test = open('test.txt',"w")
path_test = '/content/datasets/val/'

path_test_list = sorted(os.listdir(path_test+'input1/'))
random.shuffle(path_test_list)
for file_A in path_test_list:
    path_file_A = path_test+"input1/"+file_A
    path_file_B = path_test+"input2/"+file_A
    path_file_label = path_test+"mask/"+file_A
    # img = Image.open(path_file_label)
    # if not img.getbbox():
    #     print(path_file_label)
    #     continue
    file_test.write(path_file_A + ' ' + path_file_B + ' ' + path_file_label + '\n')
file_test.close()
print("ok_test")