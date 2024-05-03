from ultralytics import YOLO


def train_model():

    # Load a model
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

    # Train the model with 2 GPUs ???

    # Can add augmentation parameters here to improve model accuracy
    results = model.train(data='boss_v8.yaml', imgsz=640, epochs=20, device='mps', name='yolov8n_custom')