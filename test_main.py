import main

import pytest
import os
from tkinter import Tk


# Tests
@pytest.fixture
def app():
    # Створює екземпляр класу перед кожним тестом
    app = main.App()
    yield app
    app.destroy()


def test_app_title(app):
    assert app.title() == "Custom Select Color"


# def test_app_geometry(app):
#     assert app.geometry() == "350x700+100+100"


def test_app_resizable(app):
    assert app.resizable() == (False, False)


def test_app_primary_color_initial(app):
    assert app.color_pimary == [0, 120, 215]


def test_app_border_color_initial(app):
    assert app.color_border == [0, 102, 204]


def test_app_primary_color_hex_initial(app):
    assert app.color_pimary_hex == "#0078d7"


def test_app_border_color_hex_initial(app):
    assert app.color_border_hex == "#0066cc"


def test_app_frame_exists(app):
    assert app.frame is not None


def test_app_label_preview_exists(app):
    assert app.label_preview is not None


def test_app_canvas_exists(app):
    assert app.canvas is not None


def test_app_rect_id_exists(app):
    assert app.rect_id is not None


def test_app_color_primary_label_exists(app):
    assert app.label_color_pimary is not None


def test_app_color_primary_sliders_exist(app):
    assert app.slider_color_pimary_red is not None
    assert app.slider_color_pimary_green is not None
    assert app.slider_color_pimary_blue is not None


def test_app_color_border_label_exists(app):
    assert app.label_color_border is not None


def test_app_color_border_sliders_exist(app):
    assert app.slider_color_border_red is not None
    assert app.slider_color_border_green is not None
    assert app.slider_color_border_blue is not None


def test_app_autoinstall_checkbox_exists(app):
    assert app.checkbox_autoinstall is not None


def test_app_reload_checkbox_exists(app):
    assert app.checkbox_reload is not None


def test_app_save_preferences(app, monkeypatch):
    monkeypatch.setattr(os, 'system', lambda x: None)
    app.checkbox_autoinstall.value = True
    app.checkbox_reload.value = True

    app.save_preferences()

    # Check if the file is created
    assert os.path.exists('ChangeSelectColor.reg')

    # Check if the file content is correct
    with open('ChangeSelectColor.reg', 'r') as f:
        content = f.read().strip()
        expected_content = '''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Control Panel\Colors]
"Hilight"="0 102 204"
"HotTrackingColor"="0 120 215"'''
        assert content == expected_content


if __name__ == "__main__":
    os.environ['DISPLAY'] = ':99'

    # Run tests
    Tk().withdraw()
    pytest.main(['-vv', '--disable-warnings'])
