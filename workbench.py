#!/usr/bin/env python
"""
Workbench configuration for xblock-pdf development and testing
"""

from workbench import scenarios

# Workbench configuration
def make_workbench():
    """Create workbench for PDF XBlock"""
    return scenarios.SCENARIOS.get('pdf.pdf.PdfBlock', [
        ("PDF XBlock Demo", """
            <pdf url="http://tutorial.math.lamar.edu/pdf/Trig_Cheat_Sheet.pdf" 
                 display_name="Sample PDF Document"
                 allow_download="true"
                 source_text="Download PowerPoint"
                 source_url="http://tutorial.math.lamar.edu/pdf/Trig_Cheat_Sheet.ppt" />
        """),
        ("PDF XBlock Minimal", """
            <pdf url="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" 
                 display_name="Simple PDF" />
        """),
    ])

if __name__ == '__main__':
    # For standalone testing
    from xblock.django.request import django_to_webob_request
    from xblock.runtime import Runtime
    
    print("PDF XBlock workbench scenarios available")
    for name, xml in make_workbench():
        print(f"- {name}")
