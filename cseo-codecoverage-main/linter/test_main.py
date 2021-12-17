from linter.main import Subway

def test_sauce_selection():
    sub = Subway("tangy", "Ginger")
    sauce = sub.create_sub()
    assert "Mustard" in sauce
