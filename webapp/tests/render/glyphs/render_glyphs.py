from django.test import TestCase
from graphite.render import glyph
from mock import MagicMock

class GlyphTest(TestCase):
  def setUp(self):
    self.graph = glyph.LineGraph(data=[])
    self.graph.ctx = MagicMock(wraps=self.graph.ctx)
