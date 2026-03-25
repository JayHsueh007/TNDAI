# 分别从三个文件中导入映射字典，并给它们起别名以防冲突
from .TND_resolution_classifier import NODE_CLASS_MAPPINGS as res_mappings, NODE_DISPLAY_NAME_MAPPINGS as res_display
from .TND_aspect_ratio import NODE_CLASS_MAPPINGS as ar_mappings, NODE_DISPLAY_NAME_MAPPINGS as ar_display
from .TND_resolution_preset import NODE_CLASS_MAPPINGS as preset_mappings, NODE_DISPLAY_NAME_MAPPINGS as preset_display

# 将所有字典合并到一个总的映射中
NODE_CLASS_MAPPINGS = {
    **res_mappings,
    **ar_mappings,
    **preset_mappings
}

# 将所有显示名称合并到一个总的映射中
NODE_DISPLAY_NAME_MAPPINGS = {
    **res_display,
    **ar_display,
    **preset_display
}

# 导出给 ComfyUI 使用
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']