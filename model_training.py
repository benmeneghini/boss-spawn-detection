from ultralytics import YOLO


def train_model():

    # Load a model
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

    # Train the model with 2 GPUs ???

    # Can add augmentation parameters here to improve model accuracy
    results = model.train(data='', epochs=20, device='mps')