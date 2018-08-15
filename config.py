# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 16:45
# @Author  : Dylan
# @File    : config.py
# @Email   : wenyili@buaa.edu.cn
class Config():
    train_imgs_path = "images/train/images"
    train_labels_path = "images/train/label"
    merge_path = ""
    aug_merge_path = "deform/deform_norm2"
    aug_train_path = "deform/train/"
    aug_label_path = "deform/label/"
    test_path = "images/test"
    npy_path = "../npydata"
    result_np_save = '../results/imgs_mask_test.npy'
    save_img_path = "../results/"
    checkpoint_path = ""
    save_model_path = ""
    tensorboard_path = ""

    load_model_path = ""
    load_model = False
    model_train = True
    img_type = 'tif'
    aug_img_num = 30
    norm_size = 512
    channels = 1
    batch_size = 6

    use_gpu = "1"
    aug = True
    ratio = 0.2
    max_epoch = 200
    lr = 1e-4
    lr_reduce = 0.5
config = Config()


