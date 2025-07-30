from models.base import BaseModel
import torch

def test_model_forward():
    model = BaseModel()
    dummy_input = torch.randn(2, 10)
    out = model(dummy_input)
    assert out.shape[0] == 2