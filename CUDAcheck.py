import torch

if torch.cuda.is_available():
    device = "cuda:0"
    print("CUDA is available. Using GPU.")
else:
    device = "cpu"
    print("CUDA is not available. Using CPU.")
    
print(torch.version.cuda)

