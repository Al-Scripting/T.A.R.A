import os
os.environ["NO_TORCH_COMPILE"] = "1"

import torch

# Force-disable torch.compile globally
def dummy_compile(fn=None, **kwargs):
    return fn
torch.compile = dummy_compile
