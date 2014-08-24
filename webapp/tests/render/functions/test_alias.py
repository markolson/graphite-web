from render_functions import RenderFunctionTest
from graphite.render import functions

class AliasFunctionTest(RenderFunctionTest):

  def test_alias(self):
    seriesList = self._generate_series_list()
    substitution = "Ni!"
    results = functions.alias({}, seriesList, substitution)
    for series in results:
      self.assertEqual(series.name, substitution)
