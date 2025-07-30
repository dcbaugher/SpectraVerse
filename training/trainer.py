import pytorch_lightning as pl

def run_training(model, datamodule, config):
    trainer = pl.Trainer(
        max_epochs=config.training.max_epochs,
        accelerator="auto",
        logger=config.logger,
    )
    trainer.fit(model, datamodule=datamodule)