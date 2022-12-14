import time

import iree_torch
import torch
import torch_mlir


print("Startup complete")

print("Initializing model")
class TestModel(torch.nn.Module):
    def forward(self, num):
        return num + num

model = TestModel()
print("Model initialized")

print("Creating tensor")
st = time.time()
x = torch.randn((100000, 10000))
print(f"Done: {time.time() - st}")

print("Calling function")
st = time.time()
result = model.forward(x)
print(f"Done: {time.time() - st}")
print(result)

print("Compiling to torch_mlir")
st = time.time()
mlir = torch_mlir.compile(
    model,
    (x,),
    output_type=torch_mlir.OutputType.LINALG_ON_TENSORS)
print(f"Done: {time.time() - st}")

print("Compiling with IREE")
st = time.time()
# Backend options:
#
# llvm-cpu - cpu, native code
# vmvx - cpu, interpreted
# vulkan - GPU for general GPU devices
# cuda - GPU for NVIDIA devices
iree_backend = "cuda"
iree_vmfb = iree_torch.compile_to_vmfb(mlir, iree_backend)
print(f"Done: {time.time() - st}")

print("Loading in IREE")
st = time.time()
invoker = iree_torch.load_vmfb(iree_vmfb, iree_backend)
print(f"Done: {time.time() - st}")

print("Running on IREE")
st = time.time()
result = invoker.forward(x)
print(f"Done: {time.time() - st}")
print("RESULT:", result)