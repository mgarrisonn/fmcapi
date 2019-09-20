from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging


class SIUrlLists(APIClassTemplate):
    """
    The SIUrlLists Object in the FMC.
    """

    URL_SUFFIX = '/object/siurllists'

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SIUrlLists class.")
        self.parse_kwargs(**kwargs)

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SIUrlLists class.")

    def post(self):
        logging.info('POST method for API for SIUrlLists not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for SIUrlLists not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for SIUrlLists not supported.')
        pass
