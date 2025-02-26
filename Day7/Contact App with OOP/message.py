class Message:
    def __init__(self, sender, recipient, content, timestamp=None):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = timestamp if timestamp else self._get_current_timestamp()

    def _get_current_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")