""" Unit tests for pdf components """
# -*- coding: utf-8 -*-

# Imports ###########################################################
from __future__ import absolute_import
import json
import unittest

from mock import Mock
from workbench.runtime import WorkbenchRuntime
from xblock.runtime import DictKeyValueStore, KvsFieldData

from pdf import PdfBlock


# Constants ###########################################################
TEST_SUBMIT_DATA = {
    'display_name': "PDF Document",
    'url': "http://example.com/test.pdf",
    'allow_download': True,
    'source_text': "Download Source",
    'source_url': "http://example.com/source.ppt"
}

# Classes ###########################################################
class TestPdfBlock(unittest.TestCase):
    """ Tests for PdfBlock """

    @classmethod
    def make_pdf_block(cls):
        """ helper to construct a PdfBlock """
        runtime = WorkbenchRuntime()
        key_store = DictKeyValueStore()
        db_model = KvsFieldData(key_store)
        ids = generate_scope_ids(runtime, 'pdf')
        return PdfBlock(runtime, db_model, scope_ids=ids)

    def generate_scope_ids(self, runtime, block_type):
        """ helper to generate scope IDs """
        def_id = runtime.id_generator.create_definition(block_type)
        usage_id = runtime.id_generator.create_usage(def_id)
        return runtime.id_generator.create_scope(usage_id)

    def test_pdf_template_content(self):
        """ Test content of PdfBlock's rendered views """
        block = TestPdfBlock.make_pdf_block()
        block.usage_id = Mock()

        student_fragment = block.render('student_view', Mock())
        # pylint: disable=no-value-for-parameter
        assert '<div class="pdf-xblock-wrapper"' in student_fragment.content
        assert 'PDF Document' in student_fragment.content

        studio_fragment = block.render('studio_view', Mock())
        assert 'wrapper-comp-settings' in studio_fragment.content
        assert 'validation_alert' in studio_fragment.content

    def test_studio_pdf_submit(self):
        """ Test studio submission of PdfBlock """
        block = TestPdfBlock.make_pdf_block()

        body = json.dumps(TEST_SUBMIT_DATA)
        res = block.handle('studio_submit', make_request(body))
        # pylint: disable=no-value-for-parameter
        assert json.loads(res.body.decode('utf8'))['result'] == 'success'

        assert block.display_name == TEST_SUBMIT_DATA['display_name']
        assert block.url == TEST_SUBMIT_DATA['url']
        assert block.allow_download == TEST_SUBMIT_DATA['allow_download']

        body = json.dumps('')
        res = block.handle('studio_submit', make_request(body))
        assert json.loads(res.body.decode('utf8'))['result'] == 'error'

    def test_on_download(self):
        """ Test on_download handler"""
        block = TestPdfBlock.make_pdf_block()

        body = json.dumps({})
        res = block.handle('on_download', make_request(body))
        # pylint: disable=no-value-for-parameter
        assert json.loads(res.body.decode('utf8'))['result'] == 'success'


def generate_scope_ids(runtime, block_type):
    """ helper to generate scope IDs """
    def_id = runtime.id_generator.create_definition(block_type)
    usage_id = runtime.id_generator.create_usage(def_id)
    return runtime.id_generator.create_scope(usage_id)


def make_request(body, method='POST'):
    """ helper to make mock request """
    request = Mock()
    request.method = method
    request.body = body.encode('utf-8') if isinstance(body, str) else body
    return request
