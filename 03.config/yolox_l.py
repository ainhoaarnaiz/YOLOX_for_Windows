#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 1.0
        self.width = 1.0
        self.input_size = (1024, 1024)
        self.mosaic_scale = (0.5, 1.5)
        self.random_size = (10, 20)
        self.test_size = (1024, 1024)
        self.exp_name = os.path.split(
            os.path.realpath(__file__))[1].split(".")[0]
        self.enable_mixup = False

        # Define yourself dataset path
        # self.data_dir = "./dataset"
        # self.train_ann = "train_annotations.json"
        # self.val_ann = "validation_annotations.json"

        self.data_dir = "D:/Ainhoa/traffic_signs_data/DFG_detection/dataset_coco_ready_original_yolox"
        self.train_ann = "coco_annotations_remapped.json"
        self.val_ann = "coco_val_annotations_remapped.json"

        self.num_classes = 200 #1

        self.max_epoch = 100
        self.data_num_workers = 4
        self.eval_interval = 1
