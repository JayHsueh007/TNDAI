from .TND_resolution_classifier import NODE_CLASS_MAPPINGS as res_mappings, NODE_DISPLAY_NAME_MAPPINGS as res_display
from .TND_aspect_ratio import NODE_CLASS_MAPPINGS as ar_mappings, NODE_DISPLAY_NAME_MAPPINGS as ar_display

NODE_CLASS_MAPPINGS = {**res_mappings, **ar_mappings}
NODE_DISPLAY_NAME_MAPPINGS = {**res_display, **ar_display}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']