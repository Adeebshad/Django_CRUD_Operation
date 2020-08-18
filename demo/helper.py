from typing import Text, Dict, List

def responseFormat(success: bool, message: Text, data: Dict, errors: List) -> Dict:
    return{
        'success' : success,
        'message' : message,
        'data': data,
        'errors' : errors
    }

