def log_event(event_name, context=None):
    print(f"[LOG] {event_name}", context or {})
