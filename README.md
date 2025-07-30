# SpectraVerse

**SpectraVerse** is a modular, open-source framework for identifying molecules from spectra and generating realistic spectra from molecules. It supports deep learning pipelines, uncertainty quantification, and benchmark evaluation across spectral modalities like MS/MS and GC-MS.

---

## 🚀 Features

- Spectrum ➝ Molecule identification (MS/MS, GC-MS)
- Model zoo for deep learning architectures
- Uncertainty-aware inference
- Benchmark-ready evaluation with unit tests
- Flexible data loaders and Hydra-based config system
- Experiment tracking with Weights & Biases (WandB)
- GitHub Actions CI/CD setup

---

## 🧪 Quickstart

```bash
# Install dependencies
poetry install

# Run training with default config
poetry run python scripts/train.py
```

SpectraVerse/
├── data/                  # Loaders and transforms for spectra
├── models/                # LightningModule base and model zoo
├── training/              # Training loops and callbacks
├── evaluation/            # Metrics and benchmark loaders
├── inference/             # Inference runners with uncertainty
├── configs/               # Hydra configuration files
├── scripts/               # Entrypoints for training/inference
├── tests/                 # Unit and regression tests
├── notebooks/             # Example notebooks
├── .github/workflows/     # GitHub Actions CI
