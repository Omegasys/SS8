# tests/test_notifications.py

import pytest
from src.core.user_notifications import notify_event

def test_notify_event_console_and_log(monkeypatch):
    notifications = []

    # Mock the logger to capture logs
    class MockLogger:
        def info(self, message):
            notifications.append(("log", message))
        def warning(self, message):
            notifications.append(("warn", message))
        def error(self, message):
            notifications.append(("error", message))
    
    monkeypatch.setattr("src.utils.logger.logger", MockLogger())

    # Mock the console.print to capture console output
    console_output = []
    monkeypatch.setattr("src.core.user_notifications.console", type("MockConsole", (), {"print": lambda self, msg, **kwargs: console_output.append(msg)})())

    # Call notify_event
    notify_event(
        message_id="1234",
        source="NodeA",
        destination="NodeB",
        event_type="MESSAGE_SENT"
    )

    # Check that log was captured
    log_messages = [msg for t, msg in notifications if t == "log"]
    assert any("Message ID: 1234" in m for m in log_messages)

    # Check that console output was captured
    assert any("Message ID: 1234" in m for m in console_output)


def test_notify_event_with_webhook(monkeypatch):
    # Capture webhook payload
    webhook_called = []

    class MockResponse:
        def __init__(self):
            self.status_code = 200

    def mock_post(url, json, timeout):
        webhook_called.append(json)
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    # Call notify_event with webhook
    notify_event(
        message_id="5678",
        source="NodeC",
        destination="NodeD",
        event_type="MESSAGE_RECEIVED",
        webhook_url="http://fakewebhook.local"
    )

    # Check that webhook was called with correct data
    assert webhook_called[0]["message_id"] == "5678"
    assert webhook_called[0]["event_type"] == "MESSAGE_RECEIVED"
    assert webhook_called[0]["source"] == "NodeC"
    assert webhook_called[0]["destination"] == "NodeD"
