from render_functions import RenderFunctionTest
from graphite.render import functions

class SafeDiffFunctionTest(RenderFunctionTest):
  def test_integer_values(self):
    self.assertEqual(1, functions.safeDiff([1]))
    self.assertEqual(-1, functions.safeDiff([1,2]))
    self.assertEqual(-2, functions.safeDiff([1,2,1]))
    self.assertEqual(-5, functions.safeDiff([1,2,4]))

  def test_some_nones(self):
    self.assertEqual(1, functions.safeDiff([1,None]))
    self.assertEqual(-1, functions.safeDiff([1,None,2,None]))
    self.assertEqual(-2, functions.safeDiff([1,None,2,None,1,None]))
    self.assertEqual(-5, functions.safeDiff([1,None,2,None,4,None]))

  def test_all_nones(self):
    self.assertEqual(None, functions.safeDiff([None,None,None]))
