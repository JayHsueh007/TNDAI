import math

class ResolutionPresetNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 1920, "min": 1, "max": 8192, "step": 1}),
                "height": ("INT", {"default": 1080, "min": 1, "max": 8192, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "FLOAT", "STRING")
    RETURN_NAMES = ("res_label", "equivalent_p", "megapixels", "summary")
    FUNCTION = "analyze"
    CATEGORY = "utils"

    def analyze(self, width, height):
        pixels = width * height
        megapixels = round(pixels / 1000000, 2)
        
        # 核心算法：计算等效 16:9 的高度 (Effective P)
        # 公式：Height_eff = sqrt(Total_Pixels * 9 / 16)
        eff_p = int(math.sqrt(pixels * 9 / 16))
        
        # 定义标准梯队 (采用行业公认的切换点)
        if eff_p < 400:
            label = "360p"
        elif eff_p < 600:
            label = "480p"
        elif eff_p < 900:
            label = "720p"
        elif eff_p < 1260:
            label = "1080p"
        elif eff_p < 1800:
            label = "2K (1440p)"
        elif eff_p < 3000:
            label = "4K (2160p)"
        else:
            label = "8K+"
            
        summary = f"{label} | {eff_p}p | {megapixels}MP"
            
        return (label, eff_p, megapixels, summary)


# 导出节点映射
NODE_CLASS_MAPPINGS = {
    "ResolutionPresetNode": ResolutionPresetNode
}

# 导出节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionPresetNode": "TND Resolution Tier Identifier"
}