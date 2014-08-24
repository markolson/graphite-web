from render_functions import RenderFunctionTest
from graphite.render import functions

class SafeSumFunctionTest(RenderFunctionTest):
  def test_integer_values(self):
    self.assertEqual(10, functions.safeSum([1,2,3,4]))

  def test_some_nones(self):
    self.assertEqual(10, functions.safeSum([None,1,None,2,None,3,None,4,None,None]))

  def test_all_nones(self):
    self.assertEqual(None, functions.safeSum([None,None,None]))
