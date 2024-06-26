from .log import log_node_warn, log_node_info

class AnyType(str):
    """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

    def __eq__(self, _) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

class SelectAnyValues:
    
    NAME = 'Select Any Values'

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
           "required": {
              "enable": ("BOOLEAN", {"default": True}),
              "strategy": (["FirstEnable", "LastEnable"],),
           },
            "optional": {
                "input1": (any, {"forceInput": True}),
                "input2": (any, {"forceInput": True}),
                "input3": (any, {"forceInput": True}),
                "input4": (any, {"forceInput": True}),
                "input5": (any, {"forceInput": True}),
                "input6": (any, {"forceInput": True}),
                "input7": (any, {"forceInput": True}),
                "input8": (any, {"forceInput": True}),

            },
        }

    CATEGORY = "SelectAny"
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("output",)

    FUNCTION = "execute"

    def execute(self, enable=True,strategy=None,input1=None,input2=None, input3=None,input4=None,input5=None,input6=None, input7=None, input8=None):
        valueList = [input1, input2,input3,input4,input5,input6,input7,input8]
        if strategy == "LastEnable":
           valueList.reverse()
        for item in valueList:
           if item != None:
            return (item,)

        return (None,)