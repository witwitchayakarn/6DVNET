# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
"""Centralized catalog of paths."""

import os


class DatasetCatalog(object):
    DATA_DIR = "datasets"
    DATASETS = {
        "peku_3d_car_train": {
            "dataset_dir": "/home/wit/6dvnet/peku/train",
        },
        "peku_3d_car_val": {
            "dataset_dir": "/home/wit/6dvnet/peku/train",
        },
        "peku_3d_car_test": {
            "dataset_dir": "/home/wit/6dvnet/peku/test",
        },

        "Apollo_3d_car_train": {
            "dataset_dir": "/home/wit/6dvnet/apollo/train",
        },
        "Apollo_3d_car_val": {
            "dataset_dir": "/home/wit/6dvnet/apollo/train",
        },
        "Apollo_3d_car_test": {
            "dataset_dir": "/home/wit/6dvnet/apollo/test",
        },

        "Pascal3d+_train": {"dataset_dir": "/media/SSD_1TB/PASCAL3D+_release1.1",},
        "Pascal3d+_val": {"dataset_dir": "/media/SSD_1TB/PASCAL3D+_release1.1",},
        "Pascal3d+_test": {"dataset_dir": "/media/SSD_1TB/PASCAL3D+_release1.1",},

        "kitti_instance_train": {
            "img_dir": "/media/SSD_1TB/Kitti/data_semantics/training/image_2",
            "ann_file": "/media/SSD_1TB/Kitti/data_semantics/training/instance"
        },

        "kitti_instance_test": {
            "img_dir": "/media/SSD_1TB/Kitti/data_semantics/testing/image_2",
        },

        "kitti_train": {
            "root": "/media/SSD_1TB/Kitti/object/training",
            "img_dir": "/media/SSD_1TB/Kitti/object/training/image_2",
            "ann_file": "/media/SSD_1TB/Kitti/object/training/label_2"
        },
        "kitti_val": {
            "root": "/media/SSD_1TB/Kitti/object/training",
            "img_dir": "/media/SSD_1TB/Kitti/object/training/image_2",
            "ann_file": "/media/SSD_1TB/Kitti/object/training/label_2"
        },
        "kitti_test": {
            "img_dir": "/media/SSD_1TB/Kitti/object/testing/image_2",
        },

        "coco_2017_train": {
            "img_dir": "/media/HDD_4TB/MSCOCO/images/train2017",
            "ann_file": "/media/HDD_4TB/MSCOCO/annotations/instances_train2017.json"
        },
        "coco_2017_val": {
            "img_dir": "/media/HDD_4TB/MSCOCO/images/val2017",
            "ann_file": "/media/HDD_4TB/MSCOCO/annotations/instances_val2017.json"
        },

        "coco_2014_train": {
            "img_dir": "coco/train2014",
            "ann_file": "coco/annotations/instances_train2014.json"
        },
        "coco_2014_val": {
            "img_dir": "coco/val2014",
            "ann_file": "coco/annotations/instances_val2014.json"
        },
        "coco_2014_minival": {
            "img_dir": "coco/val2014",
            "ann_file": "coco/annotations/instances_minival2014.json"
        },
        "coco_2014_valminusminival": {
            "img_dir": "coco/val2014",
            "ann_file": "coco/annotations/instances_valminusminival2014.json"
        },
        "voc_2007_train": {
            "data_dir": "voc/VOC2007",
            "split": "train"
        },
        "voc_2007_train_cocostyle": {
            "img_dir": "voc/VOC2007/JPEGImages",
            "ann_file": "voc/VOC2007/Annotations/pascal_train2007.json"
        },
        "voc_2007_val": {
            "data_dir": "voc/VOC2007",
            "split": "val"
        },
        "voc_2007_val_cocostyle": {
            "img_dir": "voc/VOC2007/JPEGImages",
            "ann_file": "voc/VOC2007/Annotations/pascal_val2007.json"
        },
        "voc_2007_test": {
            "data_dir": "voc/VOC2007",
            "split": "test"
        },
        "voc_2007_test_cocostyle": {
            "img_dir": "voc/VOC2007/JPEGImages",
            "ann_file": "voc/VOC2007/Annotations/pascal_test2007.json"
        },
        "voc_2012_train": {
            "data_dir": "voc/VOC2012",
            "split": "train"
        },
        "voc_2012_train_cocostyle": {
            "img_dir": "voc/VOC2012/JPEGImages",
            "ann_file": "voc/VOC2012/Annotations/pascal_train2012.json"
        },
        "voc_2012_val": {
            "data_dir": "voc/VOC2012",
            "split": "val"
        },
        "voc_2012_val_cocostyle": {
            "img_dir": "voc/VOC2012/JPEGImages",
            "ann_file": "voc/VOC2012/Annotations/pascal_val2012.json"
        },
        "voc_2012_test": {
            "data_dir": "voc/VOC2012",
            "split": "test"
            # PASCAL VOC2012 doesn't made the test annotations available, so there's no json annotation
        },
        "cityscapes_fine_instanceonly_seg_train_cocostyle": {
            "img_dir": "cityscapes/images",
            "ann_file": "cityscapes/annotations/instancesonly_filtered_gtFine_train.json"
        },
        "cityscapes_fine_instanceonly_seg_val_cocostyle": {
            "img_dir": "cityscapes/images",
            "ann_file": "cityscapes/annotations/instancesonly_filtered_gtFine_val.json"
        },
        "cityscapes_fine_instanceonly_seg_test_cocostyle": {
            "img_dir": "cityscapes/images",
            "ann_file": "cityscapes/annotations/instancesonly_filtered_gtFine_test.json"
        }
    }

    @staticmethod
    def get(name):
        if "coco" in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                root=os.path.join(data_dir, attrs["img_dir"]),
                ann_file=os.path.join(data_dir, attrs["ann_file"]),
            )
            return dict(
                factory="COCODataset",
                args=args,
            )
        elif "voc" in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(data_dir, attrs["data_dir"]),
                split=attrs["split"],
            )
            return dict(
                factory="PascalVOCDataset",
                args=args,
            )
        elif "kitti_instance_train" in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                img_dir=os.path.join(data_dir, attrs['img_dir']),
                ann_file=os.path.join(data_dir, attrs['ann_file']),
            )
            return dict(
                factory='KittiInstanceDataset',
                args=args,
            )
        elif "kitti_instance_test" in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(img_dir=os.path.join(data_dir, attrs['img_dir']),)
            return dict(
                factory='KittiInstanceDataset',
                args=args,
            )
        elif "Apollo_3d_car" in name:
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(dataset_dir=attrs['dataset_dir'],
                        list_flag=name.split('_')[-1])
            return dict(
                factory='Car3D',
                args=args,
            )
        elif "peku_3d_car" in name:
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(dataset_dir=attrs['dataset_dir'],
                        list_flag=name.split('_')[-1])
            return dict(
                factory='Car3D',
                args=args,
            )
        elif "Pascal3d" in name:
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(dataset_dir=attrs['dataset_dir'],
                        list_flag=name.split('_')[-1])
            return dict(
                factory='Pascal3D',
                args=args,
            )

        raise RuntimeError("Dataset not available: {}".format(name))


class ModelCatalog(object):
    S3_C2_DETECTRON_URL = "https://dl.fbaipublicfiles.com/detectron"
    C2_IMAGENET_MODELS = {
        "MSRA/R-50": "ImageNetPretrained/MSRA/R-50.pkl",
        "MSRA/R-101": "ImageNetPretrained/MSRA/R-101.pkl",
        "FAIR/20171220/X-101-32x8d": "ImageNetPretrained/20171220/X-101-32x8d.pkl",
    }

    C2_DETECTRON_SUFFIX = "output/train/coco_2014_train%3Acoco_2014_valminusminival/generalized_rcnn/model_final.pkl"
    C2_DETECTRON_MODELS = {
        "35857197/e2e_faster_rcnn_R-50-C4_1x": "01_33_49.iAX0mXvW",
        "35857345/e2e_faster_rcnn_R-50-FPN_1x": "01_36_30.cUF7QR7I",
        "35857890/e2e_faster_rcnn_R-101-FPN_1x": "01_38_50.sNxI7sX7",
        "36761737/e2e_faster_rcnn_X-101-32x8d-FPN_1x": "06_31_39.5MIHi1fZ",
        "35858791/e2e_mask_rcnn_R-50-C4_1x": "01_45_57.ZgkA7hPB",
        "35858933/e2e_mask_rcnn_R-50-FPN_1x": "01_48_14.DzEQe4wC",
        "35861795/e2e_mask_rcnn_R-101-FPN_1x": "02_31_37.KqyEK4tT",
        "36761843/e2e_mask_rcnn_X-101-32x8d-FPN_1x": "06_35_59.RZotkLKI",
    }

    @staticmethod
    def get(name):
        if name.startswith("Caffe2Detectron/COCO"):
            return ModelCatalog.get_c2_detectron_12_2017_baselines(name)
        if name.startswith("ImageNetPretrained"):
            return ModelCatalog.get_c2_imagenet_pretrained(name)
        raise RuntimeError("model not present in the catalog {}".format(name))

    @staticmethod
    def get_c2_imagenet_pretrained(name):
        prefix = ModelCatalog.S3_C2_DETECTRON_URL
        name = name[len("ImageNetPretrained/"):]
        name = ModelCatalog.C2_IMAGENET_MODELS[name]
        url = "/".join([prefix, name])
        return url

    @staticmethod
    def get_c2_detectron_12_2017_baselines(name):
        # Detectron C2 models are stored following the structure
        # prefix/<model_id>/2012_2017_baselines/<model_name>.yaml.<signature>/suffix
        # we use as identifiers in the catalog Caffe2Detectron/COCO/<model_id>/<model_name>
        prefix = ModelCatalog.S3_C2_DETECTRON_URL
        suffix = ModelCatalog.C2_DETECTRON_SUFFIX
        # remove identification prefix
        name = name[len("Caffe2Detectron/COCO/"):]
        # split in <model_id> and <model_name>
        model_id, model_name = name.split("/")
        # parsing to make it match the url address from the Caffe2 models
        model_name = "{}.yaml".format(model_name)
        signature = ModelCatalog.C2_DETECTRON_MODELS[name]
        unique_name = ".".join([model_name, signature])
        url = "/".join([prefix, model_id, "12_2017_baselines", unique_name, suffix])
        return url
