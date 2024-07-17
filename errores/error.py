from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
import json
import inspect

# Definimos el modelo de respuesta
class UserValidationResponse(BaseModel):

    retCode: int
    retTxt: str
    additional_values: Dict[str, Any]

    def __init__(self, retCode: int, retTxt: str, **data):
        super().__init__(retCode=retCode, retTxt=retTxt, additional_values=data)
        self.log_to_file()

    def log_to_file(self):
        # Obtain the caller's frame
        caller_frame = inspect.stack()[2]
        # Get the caller method name
        caller_method = caller_frame.function
        
        # Get the caller class name if it exists
        caller_class = None
        caller_self = caller_frame.frame.f_locals.get('self', None)
        if caller_self:
            caller_class = caller_self.__class__.__name__
        
        log_entry = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "retCode": self.retCode,
            "retTxt": self.retTxt,
            "caller_method": caller_method,
            "caller_class": caller_class
        }
        log_entry.update(self.additional_values)
        
        try:
            with open("log.txt", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Error writing to file: {e}")