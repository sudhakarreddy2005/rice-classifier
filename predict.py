import torch
from model import MyModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = MyModel()
model.load_state_dict(torch.load("models/riceModel.pth", map_location=device))
model.to(device)
model.eval()

def predict(input_data):
    with torch.inference_mode():
        input_tensor = torch.tensor(input_data, dtype=torch.float32).unsqueeze(0).to(device)
        output = model(input_tensor)
        pred = (output > 0.5).float()
    return int(pred.item())