"""
Tests for PDF XBlock
"""
import unittest
from unittest.mock import Mock, patch

from xblock.test.tools import TestRuntime

from pdf.pdf import PdfBlock


class TestPdfBlock(unittest.TestCase):
    """Test PdfBlock functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.runtime = TestRuntime()
        self.block = PdfBlock(self.runtime, scope_ids=Mock())

    def test_init(self):
        """Test block initialization"""
        self.assertEqual(self.block.display_name, "PDF")
        self.assertEqual(self.block.allow_download, True)
        self.assertEqual(self.block.icon_class, "other")

    def test_student_view(self):
        """Test student view rendering"""
        self.block.url = "http://example.com/test.pdf"
        
        with patch.object(self.block, 'render_template') as mock_render:
            mock_render.return_value = "<div>PDF Content</div>"
            
            fragment = self.block.student_view()
            
            self.assertIsNotNone(fragment)
            mock_render.assert_called_once()

    def test_studio_view(self):
        """Test studio view rendering"""
        with patch.object(self.block, 'render_template') as mock_render:
            mock_render.return_value = "<div>Studio Content</div>"
            
            fragment = self.block.studio_view()
            
            self.assertIsNotNone(fragment)
            mock_render.assert_called_once()

    def test_save_pdf(self):
        """Test save_pdf handler"""
        data = {
            'display_name': 'Test PDF',
            'url': 'http://example.com/test.pdf',
            'allow_download': 'True',
            'source_text': 'Download Source',
            'source_url': 'http://example.com/source.ppt'
        }
        
        result = self.block.save_pdf(data)
        
        self.assertEqual(result['result'], 'success')
        self.assertEqual(self.block.display_name, 'Test PDF')
        self.assertEqual(self.block.url, 'http://example.com/test.pdf')
        self.assertTrue(self.block.allow_download)

    def test_on_download(self):
        """Test on_download handler"""
        with patch.object(self.block.runtime, 'publish') as mock_publish:
            result = self.block.on_download({})
            
            self.assertEqual(result['result'], 'success')
            mock_publish.assert_called_once()

if __name__ == '__main__':
    unittest.main()
