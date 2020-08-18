class RequestError(object):
    METHOD_NOT_ALLOWED ={
        'code': 1,
        'message': 'Requested method is not allow.'
    }
    INVALID_REQUEST_FORMAT = {
        'code': 2,
        'message' : 'User request is not properly formatted.'
    }

class DatabaseError(object):
    DATA_ERROR = {
        'code' : 3,
        'message' : 'No data exits on the database.'
    }