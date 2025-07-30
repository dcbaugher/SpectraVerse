import hydra
from omegaconf import DictConfig
from pytorch_lightning import seed_everything
from training.trainer import run_training
from models.base import BaseModel
from data.datamodule import DummyDataModule
from pytorch_lightning.loggers import WandbLogger

@hydra.main(config_path="../configs", config_name="default", version_base="1.3")
def main(cfg: DictConfig):
    seed_everything(42)

    model = BaseModel()
    datamodule = DummyDataModule(batch_size=cfg.training.batch_size)
    cfg.logger = WandbLogger(project="spectraverse", log_model=True)

    run_training(model, datamodule, cfg)

if __name__ == "__main__":
    main()