"""test log-html"""
import sys
import os

import pytest

from logToHtml import main, parse_log_file

LOG_DIR = os.path.join(os.path.dirname(__file__), "data", "logs")


def test_main(monkeypatch):
    html_file = "test_html.html"
    args = [
        "logToHtml.py",
        LOG_DIR,
        html_file,
    ]

    monkeypatch.setattr(sys, 'argv', args)

    assert main() is None

    html_file_path = os.path.join(os.path.dirname(LOG_DIR), html_file)

    assert os.path.isfile(html_file_path)

    # clean up html file
    os.remove(html_file_path)


@pytest.mark.parametrize(
    "log_file,expected_status",
    [
        ("error_first.log", "SUCCESS"),
        ("error_last.log", "ERROR"),
    ]
)
def test_parse_log_file(log_file, expected_status):
    log_file_path = os.path.join(LOG_DIR, log_file)

    _, _, status = parse_log_file(log_file_path)

    assert status == expected_status




