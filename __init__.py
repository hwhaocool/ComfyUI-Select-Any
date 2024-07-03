
from .nodes import SelectAnyValues

import torch
print("torch version :" + torch.__version__)
print("cuda version :" + torch.version.cuda)
print("cudnn version :" + str(torch.backends.cudnn.version()))

NODE_CLASS_MAPPINGS = {
    "SelectAnyValues": SelectAnyValues,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SelectAnyValues": "Select Any Values Node",
}

# WEB_DIRECTORY = "./web"