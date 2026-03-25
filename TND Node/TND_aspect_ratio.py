import math

class AspectRatioNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {
                    "default": 1920,
                    "min": 1,
                    "max": 10000,
                    "step": 1
                }),
                "height": ("INT", {
                    "default": 1080,
                    "min": 1,
                    "max": 10000,
                    "step": 1
                }),
            }
        }

    RETURN_TYPES = ("STRING", "FLOAT", "STRING")
    RETURN_NAMES = ("ratio_string", "ratio_float", "orientation")
    FUNCTION = "calculate"
    CATEGORY = "utils"

    def calculate(self, width, height):
        # 防止除0
        if height == 0:
            return ("invalid", 0.0, "invalid")

        # 最大公约数
        gcd = math.gcd(width, height)

        ratio_w = width // gcd
        ratio_h = height // gcd

        ratio_string = f"{ratio_w}:{ratio_h}"
        ratio_float = width / height

        # 判断方向
        if width > height:
            orientation = "landscape"
        elif width < height:
            orientation = "portrait"
        else:
            orientation = "square"

        return (ratio_string, ratio_float, orientation)


# 注册节点
NODE_CLASS_MAPPINGS = {
    "AspectRatioNode": AspectRatioNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AspectRatioNode": "TND Aspect Ratio Calculator"
}
