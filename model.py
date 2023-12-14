from torch import nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, image_height: int, image_width: int, num_actions: int):
        super(Net, self).__init__()
        h = image_height
        w = image_width
        self.c1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.pool1 = nn.MaxPool2d(4)
        h //= 4
        w //= 4
        self.c2 = nn.Conv2d(16, 16, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(4)
        h //= 4
        w //= 4
        self.head1 = nn.Linear(h * w * 16, num_actions)
        return

    def forward(self, x):
        batch_size = x.size(0)
        x = self.c1(x)
        x = self.pool1(x)
        x = F.relu(x)
        x = self.c2(x)
        x = self.pool2(x)
        x = F.relu(x)
        x = x.view(batch_size, -1)
        x = self.head1(x)
        return x
