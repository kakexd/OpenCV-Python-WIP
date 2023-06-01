import cv2
import os
import numpy as np

class CascadeTrain:
    def __init__(self, positive_images_dir, negative_images_dir, cascade_file):
        self.positive_images_dir = positive_images_dir
        self.negative_images_dir = negative_images_dir
        self.cascade_file = cascade_file

    def train(self, image_size=(24, 24), num_stages=20, min_hit_rate=0.995, max_false_alarm_rate=0.5):
        positive_images, annotations = self.load_positive_images()

        annotations = np.array(annotations)

        trainer = cv2.CascadeClassifier_TrainCascade()

        params = cv2.CascadeClassifier_TrainCascadeParams()
        params.stageParams.numPos = len(positive_images)
        params.stageParams.numNeg = len(os.listdir(self.negative_images_dir))
        params.stageParams.minHitRate = min_hit_rate
        params.stageParams.maxFalseAlarmRate = max_false_alarm_rate
        params.numStages = num_stages
        params.featureParams.maxDepth = 1

        cascade = trainer.train(positive_images, annotations, self.negative_images_dir, params)

        cascade.save(self.cascade_file)

    def load_positive_images(self):
        positive_images = []
        annotations = []

        for img_file in os.listdir(self.positive_images_dir):
            if img_file.endswith('.jpg'):
                img_path = os.path.join(self.positive_images_dir, img_file)
                annotation_file = os.path.splitext(img_file)[0] + '.txt'
                annotation_path = os.path.join(self.positive_images_dir, annotation_file)

                img = cv2.imread(img_path)

                with open(annotation_path, 'r') as f:
                    annotation = f.readline().strip().split(',')

                x, y, w, h = map(int, annotation)

                positive_images.append(img)
                annotations.append((x, y, w, h))

        return positive_images, annotations