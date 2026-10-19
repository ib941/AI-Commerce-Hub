from streamlit.testing.v1 import AppTest

def test_app_runs_and_renders():
    """Test that the app runs without exceptions and renders the main components."""
    at = AppTest.from_file("portfolio_hub.py").run()

    assert not at.exception
    assert at.sidebar

def test_navigation_portfolio():
    at = AppTest.from_file("portfolio_hub.py").run()

    # Check if the title text exists
    assert any("Ibrahim Alkabsi" in md.value for md in at.markdown)
    assert any("Complete Solutions Center" in md.value for md in at.markdown)

def test_navigation_ecommerce():
    at = AppTest.from_file("portfolio_hub.py").run()

    # Select E-Commerce Hub
    at.sidebar.radio[0].set_value("🛍️  E-Commerce Hub").run()

    assert any("E-Commerce Content Hub" in md.value for md in at.markdown)
    assert any("Upload Product Image" in uploader.label for uploader in at.file_uploader)

def test_navigation_storyboard():
    at = AppTest.from_file("portfolio_hub.py").run()

    # Select Storyboard Architect
    at.sidebar.radio[0].set_value("🎬  Storyboard Architect").run()

    assert any("Cinematic Storyboard Architect" in md.value for md in at.markdown)
    assert any("Brand / Product Name" in text_input.label for text_input in at.text_input)
