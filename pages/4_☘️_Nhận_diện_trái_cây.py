import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
import os

import Custome.custome as cs
from object_detection.utils import config_util
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

cs.ChangeTheme("NHẬN DIỆN TRÁI CÂY","🍊")

@tf.function
def detect_fn(image):
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)
    return detections


def xoa_trung(a, L):
    index = []
    flag = np.zeros(L, np.bool)
    for i in range(L):
        if flag[i] == False:
            flag[i] = True
            x1 = (a[i, 0] + a[i, 2]) / 2
            y1 = (a[i, 1] + a[i, 3]) / 2
            for j in range(i + 1, L):
                x2 = (a[j, 0] + a[j, 2]) / 2
                y2 = (a[j, 1] + a[j, 3]) / 2
                d = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if d < 0.2:
                    flag[j] = True
            index.append(i)
    for i in range(L):
        if i not in index:
            flag[i] = False
    return flag


def main():
    file = st.file_uploader("Upload an image", type=["jpg", "tif", "bmp", "gif", "png"])

    if file is not None:
        imgin = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        detections = detect_fn(tf.convert_to_tensor(np.expand_dims(imgin, 0), dtype=tf.float32))

        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                      for key, value in detections.items()}
        detections['num_detections'] = num_detections

        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

        label_id_offset = 1
        image_np_with_detections = imgin.copy()

        my_box = detections['detection_boxes']
        my_class = detections['detection_classes'] + label_id_offset
        my_score = detections['detection_scores']

        my_score = my_score[my_score >= 0.7]
        L = len(my_score)
        my_box = my_box[0:L]
        my_class = my_class[0:L]

        flagTrung = xoa_trung(my_box, L)
        my_box = my_box[flagTrung]
        my_class = my_class[flagTrung]
        my_score = my_score[flagTrung]

        viz_utils.visualize_boxes_and_labels_on_image_array(
            image_np_with_detections,
            my_box,
            my_class,
            my_score,
            category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=5,
            min_score_thresh=.7,
            agnostic_mode=False)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Ảnh ban đầu")
            st.image(imgin, channels="BGR", width=350)

        with col2:
            st.subheader("Ảnh được nhận dạng")
            st.image(image_np_with_detections, channels="BGR", width=350)


CONFIG_PATH = 'FruitRecognition/Tensorflow/workspace/models_TTD/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = 'FruitRecognition/Tensorflow/workspace/models_TTD/my_ssd_mobnet/'
ANNOTATION_PATH = 'FruitRecognition/Tensorflow/workspace/annotations'

configs = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
detection_model = model_builder.build(model_config=configs['model'], is_training=False)
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-6')).expect_partial()
category_index = label_map_util.create_category_index_from_labelmap(ANNOTATION_PATH + '/label_map.pbtxt')

if __name__ == '__main__':
    main()
