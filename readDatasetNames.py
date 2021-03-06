import os

phase = "train"
root_folder = "./dataset/AidedDeblur/" + phase + "/"
file_list = os.listdir(root_folder)
instance_names = set([f[:6] for f in file_list if '.png' in f])

f_original = open("./dataset/AidedDeblur/" + phase + "_instance_names.txt", "w+")
for name in sorted(list(instance_names)):
    f_original.write(root_folder + name + "\r\n")
f_original.close()

f_train = open("./dataset/AidedDeblur/" + phase + "_instance_names.txt", "r")
train_data_name = f_train.readlines()
f_train.close()
print('Number of Train Sets:')
print(len(instance_names))

phase = "test"
root_folder = "./dataset/AidedDeblur/" + phase + "/"
file_list = os.listdir(root_folder)
instance_names = set([f[:6] for f in file_list if '.png' in f])

f_original = open("./dataset/AidedDeblur/" + phase + "_instance_names.txt", "w+")
for name in sorted(list(instance_names)):
    f_original.write(root_folder + name + "\r\n")
f_original.close()

f_train = open("./dataset/AidedDeblur/" + phase + "_instance_names.txt", "r")
train_data_name = f_train.readlines()
f_train.close()

print('Number of Test Sets:')
print(len(instance_names))
