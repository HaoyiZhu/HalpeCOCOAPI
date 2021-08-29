## Halpe-COCO API: COCO API for [Halpe-FullBody dataset](https://github.com/Fang-Haoshu/Halpe-FullBody)
- We get this API by modifying the [COCO API](https://github.com/cocodataset/cocoapi) to adapt to the Halpe-FullBody dataset.

## Details:
- Modify the function showAnns in [PythonAPI/pycocotools/coco.py](PythonAPI/pycocotools/coco.py#L233) so that it can show 136 full body keypoints.
- Modify the evaluation code in [PythonAPI/pycocotools/cocoeval.py](PythonAPI/pycocotools/cocoeval.py) to adapt to the 136-keypoints case.

## To install:

- Run `pip install halpecocotools`.

