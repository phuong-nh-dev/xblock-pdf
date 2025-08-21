"""
Workbench settings for PDF XBlock.
"""

from xblock.reference.plugins import Service, default_services
from workbench import settings_base

# Use the workbench settings as our base
globals().update(settings_base.__dict__)

# Add our XBlock
INSTALLED_APPS.extend([
    'pdf',
])

# Configure XBlock
XBLOCK_SELECT_FUNCTION = lambda block_type: (
    block_type in ['pdf']
)

# XBlock configuration
XBLOCKS = {
    'pdf': 'pdf.pdf:PdfBlock',
}