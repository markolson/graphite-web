from django.test import TestCase
from graphite.render.datalib import TimeSeries

class RenderFunctionTest(TestCase):
  def setUp(self):
    pass

  def _generate_series_list(self):
    seriesList = []
    config = [range(101), range(101), [1, None, None, None, None]]

    for i, c in enumerate(config):
        name = "collectd.test-db{0}.load.value".format(i + 1)
        seriesList.append(TimeSeries(name, 0, 1, 1, c))
    return seriesList

  def _verify_series_options(self, seriesList, name, value):
    """
    Verify a given option is set and True for each series in a
    series list
    """
    for series in seriesList:
        self.assertIn(name, series.options)
        if value is True:
            test_func = self.assertTrue
        else:
            test_func = self.assertEqual

        test_func(series.options.get(name), value)

  def _generate_mr_series(self):
    seriesList = [
        TimeSeries('group.server1.metric1',0,1,1,[None]),
        TimeSeries('group.server1.metric2',0,1,1,[None]),
        TimeSeries('group.server2.metric1',0,1,1,[None]),
        TimeSeries('group.server2.metric2',0,1,1,[None]),
    ]
    mappedResult = [
        [seriesList[0],seriesList[1]],
        [seriesList[2],seriesList[3]]
    ]
    return (seriesList,mappedResult)
