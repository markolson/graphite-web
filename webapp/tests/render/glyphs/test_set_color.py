from render_glyphs import GlyphTest

class SetColorGlyphTest(GlyphTest):

  def test_valid_htmlcolor(self):
    self.graph.setColor('white')
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 1.0, 1.0, 1.0)

  def test_invalid_htmlcolor(self):
    # if this string is >= 6 chars, it fails earlier on a hex conversion
    self.assertRaises(ValueError, self.graph.setColor, 'mud')

  def test_valid_rgb(self):
    self.graph.setColor((255,0,51))
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 0.0, 0.2, 1.0)

  def test_rgb_and_alpha(self):
    self.graph.setColor((255,0,51), alpha=0.4)
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 0.0, 0.2, 0.4)

  def test_invalid_rgb(self):
    self.assertRaises(ValueError, self.graph.setColor, (255,0))

  def test_hex(self):
    self.graph.setColor('FF0033')
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 0.0, 0.2, 1.0)

  def test_hex_and_octothorp(self):
    self.graph.setColor('#FF0033')
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 0.0, 0.2, 1.0)

  def test_hex_with_alpha(self):
    self.graph.setColor('FF003399')
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 0.0, 0.2, 0.6)

  def test_hex_with_forced_alpha(self):
    self.graph.setColor('FF0033FF', alpha=0.4, forceAlpha=True)
    self.graph.ctx.set_source_rgba.assert_called_with(1.0, 0.0, 0.2, 0.4)
