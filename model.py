import torch.nn as nn

INPUT_SIZE = 10   # ⚠️ change if your dataset has different features
HIDDEN_NEURONS = 10

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.input_layer = nn.Linear(INPUT_SIZE, HIDDEN_NEURONS)
        self.linear = nn.Linear(HIDDEN_NEURONS, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.input_layer(x)
        x = self.linear(x)
        x = self.sigmoid(x)
        return x