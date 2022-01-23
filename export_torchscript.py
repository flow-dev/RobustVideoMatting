"""
Export TorchScript
    python export_torchscript.py \
        --variant mobilenetv3 \
        --checkpoint "PATH_TO_CHECKPOINT" \
        --precision float16 \
        --output "torchscript.pth"
"""

import argparse
import torch
from model import MattingNetwork

# --------------- Arguments ---------------


parser = argparse.ArgumentParser(description='Export TorchScript')

parser.add_argument('--variant', type=str, required=True, choices=['mobilenetv3', 'resnet50'])
parser.add_argument('--checkpoint', type=str, required=True)
parser.add_argument('--precision', type=str, default='float16', choices=['float32', 'float16'])
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

# --------------- Main ---------------

model = MattingNetwork(args.variant).eval()
model.load_state_dict(torch.load(args.checkpoint, map_location='cpu'))
for p in model.parameters():
    p.requires_grad = False
    
if args.precision == 'float16':
    model = model.half()
    
model = torch.jit.script(model)

if args.precision == 'float16':
    output_filename = "RVM_" + args.variant + "_fp16_" + args.output
else:
    output_filename = "RVM_" + args.variant + "_fp32_" + args.output

print(output_filename)
model.save(output_filename)

# --------------- Test ---------------

print("####### [Start:] Test Print Model Code #######")
test_model = torch.jit.load(output_filename)
print(test_model.code)
print("####### [End:] Test Print Model Code #######")
