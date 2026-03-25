import gc
import torch

def gpu_mem(x):
    if isinstance(x, torch.Tensor) and x.is_cuda:
        return x.element_size() * x.nelement() / 1024**2
    return 0

def dump_tensors():
    total = 0
    for obj in gc.get_objects():
        try:
            if torch.is_tensor(obj) and obj.is_cuda:
                size = obj.element_size() * obj.nelement() / 1024**2
                total += size
                print(type(obj), obj.size(), f"{size:.2f} MB")
        except:
            pass
    print(f"\nTotal GPU memory tracked: {total:.2f} MB")