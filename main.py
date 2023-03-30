import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_default_device(device)
print(device)
tensorA = torch.rand(size=(4, 5, 3))
tensorB = torch.rand(size=(4, 5, 3))

