# demo_notifications.py

from src.core.user_notifications import notify_event

def main():
    print("Demo: Notification System\n")

    # Simulated events
    events = [
        {"message_id": "MSG001", "source": "NodeA", "destination": "NodeB", "event_type": "MESSAGE_SENT"},
        {"message_id": "MSG002", "source": "NodeB", "destination": "NodeC", "event_type": "MESSAGE_RECEIVED"},
        {"message_id": "MSG003", "source": "NodeC", "destination": "NodeD", "event_type": "MESSAGE_SENT"},
    ]

    # Trigger notifications for each event
    for event in events:
        notify_event(
            message_id=event["message_id"],
            source=event["source"],
            destination=event["destination"],
            event_type=event["event_type"]
            # webhook_url="https://example.com/webhook"  # Optional
        )

    print("\nDemo complete.")

if __name__ == "__main__":
    main()
