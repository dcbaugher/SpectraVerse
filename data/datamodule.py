from pytorch_lightning import LightningDataModule
from torch.utils.data import DataLoader
from data.dummy_dataset import DummySpectrumDataset

class DummyDataModule(LightningDataModule):
    def __init__(self, batch_size=32):
        super().__init__()
        self.batch_size = batch_size

    def setup(self, stage=None):
        self.train_dataset = DummySpectrumDataset()
        self.val_dataset = DummySpectrumDataset()

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)