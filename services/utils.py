from flask import request
from flask_restful import Resource
from src.response import ResponseData
from src.querybase.contact import Contact
from src.main_logger import set_up_logging


response = ResponseData()
logger = set_up_logging()


class Home(Resource):
    @staticmethod
    def get():
        return response.http_200(data={"message": "Success OK 200"})

    @staticmethod
    def post():
        return response.http_405(error=True)


class ContactUs(Resource):
    @staticmethod
    def post():
        data = request.get_json()['data']
        inserted = Contact.concerns(**data)
        logger.info(f"Contact information update status: {inserted}")
        if inserted:
            return response.http_200(data={"message": "Thanks for contacting us, We will send response mail soon."},
                                     error=False)
        return response.http_503(data={
            "message": "Due to some technical issue, We are not able to process this request."}, error=True)
