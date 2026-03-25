class ResolutionClassifier:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {
                    "default": 1024,
                    "min": 1,
                    "max": 10000,
                    "step": 1
                }),
                "height": ("INT", {
                    "default": 1024,
                    "min": 1,
                    "max": 10000,
                    "step": 1
                }),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("resolution_label", "long_edge")

    FUNCTION = "classify"
    CATEGORY = "utils"

    def classify(self, width, height):
        long_edge = max(width, height)

        if long_edge < 1920:
            label = "1k"
        elif long_edge < 2560:
            label = "2k"
        elif long_edge < 3840:
            label = "3k"
        else:
            label = "4k"

        return (label, long_edge)


NODE_CLASS_MAPPINGS = {
    "ResolutionClassifier": ResolutionClassifier
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionClassifier": "TND Resolution Classifier (1K/2K/3K/4K)"
}
