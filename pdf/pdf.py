"""PDF XBlock main Python class - Updated for OpenEDX Teak compatibility"""

import pkg_resources
import logging

from django.utils.translation import gettext_lazy as _

from xblock.core import XBlock
from xblock.fields import Scope, String, Boolean
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

log = logging.getLogger(__name__)
loader = ResourceLoader(__name__)


class PdfBlock(StudioEditableXBlockMixin, XBlock):
    """
    PDF XBlock for embedding PDF documents in courses.
    Compatible with OpenEDX Teak release and XBlock 2.0+.
    """

    """
    Icon of the XBlock. Values : [other (default), video, problem]
    """
    icon_class = "other"
    
    # Enable studio editing
    has_author_view = True

    # Studio editable fields
    editable_fields = ('display_name', 'url', 'allow_download', 'source_text', 'source_url')

    # Fields
    display_name = String(
        display_name=_("Display Name"),
        default=_("PDF"),
        scope=Scope.settings,
        help=_("This name appears in the horizontal navigation at the top of the page.")
    )

    url = String(
        display_name=_("PDF URL"),
        default="http://tutorial.math.lamar.edu/pdf/Trig_Cheat_Sheet.pdf",
        scope=Scope.content,
        help=_("The URL for your PDF.")
    )

    allow_download = Boolean(
        display_name=_("PDF Download Allowed"),
        default=True,
        scope=Scope.content,
        help=_("Display a download button for this PDF.")
    )

    source_text = String(
        display_name=_("Source document button text"),
        default="",
        scope=Scope.content,
        help=_("Add a download link for the source file of your PDF. "
               "Use it for example to provide the PowerPoint file used to create this PDF.")
    )

    source_url = String(
        display_name=_("Source document URL"),
        default="",
        scope=Scope.content,
        help=_("Add a download link for the source file of your PDF. "
               "Use it for example to provide the PowerPoint file used to create this PDF.")
    )

    # XBlock 2.0+ compatibility
    @property
    def block_id(self):
        """Return block ID for XBlock 2.0+ compatibility"""
        return getattr(self.scope_ids, 'usage_id', None)
    
    @property
    def block_type(self):
        """Return block type for XBlock 2.0+ compatibility"""
        return 'pdf'

    # Util functions
    def load_resource(self, resource_path):
        """
        Gets the content of a resource using modern XBlock utils
        """
        try:
            return loader.load_unicode(resource_path)
        except Exception as e:
            log.warning("Failed to load resource %s: %s", resource_path, e)
            # Fallback to pkg_resources for compatibility
            try:
                resource_content = pkg_resources.resource_string(__name__, resource_path)
                return resource_content.decode("utf8")
            except Exception as fallback_e:
                log.error("Fallback resource loading failed for %s: %s", resource_path, fallback_e)
                return ""

    def render_template(self, template_path, context=None):
        """
        Evaluate a template by resource path, applying the provided context
        """
        if context is None:
            context = {}
        try:
            return loader.render_django_template(template_path, context)
        except Exception as e:
            log.warning("Failed to render template %s: %s", template_path, e)
            # Fallback to simple template loading
            template_str = self.load_resource(template_path)
            # Simple template variable substitution for fallback
            for key, value in context.items():
                template_str = template_str.replace('{{ ' + key + ' }}', str(value))
            return template_str

    # Main functions
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """

        context = {
            'display_name': self.display_name,
            'url': self.url,
            'allow_download': self.allow_download,
            'source_text': self.source_text,
            'source_url': self.source_url
        }
        html = self.render_template('static/html/pdf_view.html', context)
        
        # Log the PDF loading event
        try:
            event_type = 'edx.pdf.loaded'
            event_data = {
                'url': self.url,
                'source_url': self.source_url,
            }
            self.runtime.publish(self, event_type, event_data)
        except Exception as e:
            log.warning("Failed to publish PDF loaded event: %s", e)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/pdf_view.js"))
        frag.initialize_js('pdfXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url,
            'allow_download': self.allow_download,
            'source_text': self.source_text,
            'source_url': self.source_url
        }
        html = self.render_template('static/html/pdf_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/pdf_edit.js"))
        frag.initialize_js('pdfXBlockInitEdit')
        return frag

    @XBlock.json_handler
    def on_download(self, data, suffix=''):
        """
        The download file event handler
        """
        try:
            event_type = 'edx.pdf.downloaded'
            event_data = {
                'url': self.url,
                'source_url': self.source_url,
            }
            self.runtime.publish(self, event_type, event_data)
            return {'result': 'success'}
        except Exception as e:
            log.warning("Failed to publish PDF downloaded event: %s", e)
            return {'result': 'error', 'message': str(e)}

    @XBlock.json_handler
    def save_pdf(self, data, suffix=''):
        """
        The saving handler.
        """
        try:
            self.display_name = data.get('display_name', self.display_name)
            self.url = data.get('url', self.url)
            self.allow_download = data.get('allow_download', 'True') == "True"  # Str to Bool translation
            self.source_text = data.get('source_text', self.source_text)
            self.source_url = data.get('source_url', self.source_url)

            return {'result': 'success'}
        except Exception as e:
            log.error("Failed to save PDF settings: %s", e)
            return {'result': 'error', 'message': str(e)}
