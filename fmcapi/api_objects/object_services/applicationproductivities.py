from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
import logging
import warnings


class ApplicationProductivities(APIClassTemplate):
    """
    The ApplicationProductivities Object in the FMC.
    """

    URL_SUFFIX = '/object/applicationproductivities'
    VALID_CHARACTERS_FOR_NAME = """[.\w\d_\- ]"""

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for ApplicationProductivities class.")
        self.parse_kwargs(**kwargs)

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for ApplicationProductivities class.")

    def post(self):
        logging.info('POST method for API for ApplicationProductivities not supported.')
        pass

    def put(self):
        logging.info('PUT method for API for ApplicationProductivities not supported.')
        pass

    def delete(self):
        logging.info('DELETE method for API for ApplicationProductivities not supported.')
        pass


class ApplicationProductivity(ApplicationProductivities):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: ApplicationProductivity() should be called via ApplicationProductivities().")
        super().__init__(fmc, **kwargs)
