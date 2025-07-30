from torch.utils.data import Dataset
import torch

class DummySpectrumDataset(Dataset):
    def __init__(self, num_samples=100, input_dim=10):
        self.data = torch.randn(num_samples, input_dim)
        self.labels = torch.randint(0, 5, (num_samples,))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]