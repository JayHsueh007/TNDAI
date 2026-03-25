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

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("resolution_label", "width", "height")
    FUNCTION = "identify"
    CATEGORY = "utils"

    def identify(self, width, height):
        # 使用长边 (Long Side) 作为判断基准
        long_side = max(width, height)
        
        # 根据工业标准长边进行区间划分 (取中值作为切换点)
        # 480p 宽通常是 854
        # 720p 宽通常是 1280
        # 1080p 宽通常是 1920
        # 2K 宽通常是 2560
        # 4K 宽通常是 3840
        
        if long_side <= 1000:       # 接近 854
            res_label = "480p"
        elif long_side <= 1500:     # 接近 1280 (你提到的 960x1280 就在这个区间)
            res_label = "720p"
        elif long_side <= 2200:     # 接近 1920
            res_label = "1080p"
        elif long_side <= 3200:     # 接近 2560
            res_label = "2K"
        elif long_side <= 5000:     # 接近 3840
            res_label = "4K"
        else:
            res_label = "8K+"
            
        return (res_label, width, height)

# 导出节点映射
NODE_CLASS_MAPPINGS = {
    "ResolutionPresetNode": ResolutionPresetNode
}

# 导出节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionPresetNode": "TND Resolution Tier Identifier"
}