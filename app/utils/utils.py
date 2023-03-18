import numpy as np
from detectron2 import model_zoo
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import app.utils.config as config
from io import BytesIO
import PIL


cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.DEVICE = 'cpu'
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS =  config.cfg.clusters.path
cluster_predictor = DefaultPredictor(cfg)
cfg.MODEL.WEIGHTS =  config.cfg.penducles.path
penducle_predictor = DefaultPredictor(cfg)


def make_prediction(image, service):

    resized_image = image.resize((600, 400))
    pil_array = np.array(resized_image)

    if service == 'clusters':
        outputs = cluster_predictor(pil_array)
        metadata=config.cfg.clusters.metadata
    else:
        outputs = penducle_predictor(pil_array)
        metadata=config.cfg.penducles.metadata

    v = Visualizer(
            pil_array,
            metadata=metadata,
            instance_mode=ColorMode.IMAGE_BW  
        )

    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    pred = v.get_image()
    prediction_img = PIL.Image.fromarray(pred)

    with BytesIO() as output:
        prediction_img.save(output, 'BMP')
        data1 = output.getvalue()
    
    return data1

