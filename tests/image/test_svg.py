# encoding: utf-8

"""Unit test suite for docx.image.svg module"""

from __future__ import absolute_import, print_function

import pytest

from docx.compat import BytesIO
from docx.image.constants import MIME_TYPE
from docx.image.svg import Svg

from ..unitutil.file import test_file
from ..unitutil.mock import ANY, initializer_mock

class DescribeSvg(object):

    @pytest.fixture
    def sample_stream(self):
      with open(test_file('test.svg'), 'rb') as f:
        blob = f.read()
        return blob

    def it_can_construct_from_a_svg_stream(self, Svg__init__, sample_stream):
        stream = BytesIO(sample_stream)
        svg = Svg.from_stream(stream)

        Svg__init__.assert_called_once_with(
          ANY, 81.56884, 17.054602, 72, 72)
        assert isinstance(svg, Svg)

    def it_knows_its_content_type(self):
        svg = Svg(None, None, None, None)
        assert svg.content_type == MIME_TYPE.SVG

    def it_knows_its_default_ext(self):
        svg = Svg(None, None, None, None)
        assert svg.default_ext == 'svg'

    # fixture components ---------------------------------------------

    @pytest.fixture
    def Svg__init__(self, request):
        return initializer_mock(request, Svg)
