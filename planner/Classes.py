import json_resp as j

class Event:


    def __init__(self, id, date, time, text):

        self.id = id
        self.date = date
        self.time = time
        self.text = text 
        self._status = True

    def __str__(self):

       return (f'{self.date}   {self.time}    {self.text}')
    

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create an Event instance from a dict loaded from JSON.
        Accepts both 'Id'/'Date'... and 'id'/'date'... keys.
        """
        # support different key styles
        _id = data.get("Id", data.get("id"))
        date = data.get("Date", data.get("date"))
        time = data.get("Time", data.get("time"))
        text = data.get("Text", data.get("text"))

        # status should ideally be bool in storage; accept string too
        raw_status = data.get("Status", data.get("status", True))
        if isinstance(raw_status, str):
            raw_status = raw_status.strip().lower() in ("ativado", "true", "1", "yes", "y", "on")

        return cls(id=_id, date=date, time=time, text=text, status=raw_status)

    def to_dict(self) -> dict:
        """
        Convert the Event to a dict to be saved in JSON.
        Stores Status as bool (recommended for persistence).
        """
        return {
            "Id": self.id,
            "Date": self.date,
            "Time": self.time,
            "Text": self.text,
            "Status": self._status,
        }

    

    @property
    #property e sobre alteracoes que fazemos com o obj.
    def status(self):

        return 'ativado' if self._status else 'desativado'
    

