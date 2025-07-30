import pytorch_lightning as pl
import torch.nn as nn

class BaseModel(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = nn.Identity()  # replace with actual architecture

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        # TODO: implement
        pass

    def configure_optimizers(self):
        # TODO: return optimizer(s)
        return []