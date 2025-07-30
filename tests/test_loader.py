import pytest
from data.loaders import mzml_loader

def test_mzml_loader_not_implemented():
    with pytest.raises(NotImplementedError):
        mzml_loader.load_mzml("test.mzML")