import torch

if torch.cuda.is_available():
    device = "cuda:0"
    print("CUDA is available. Using GPU.")
    print(f"Torch CUDA version {torch.version.cuda}")
else:
    device = "cpu"
    print("CUDA is not available. Using CPU.")
    
print(torch.version.cuda)

