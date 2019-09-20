from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
from fmcapi.api_objects.helper_functions import validate_vlans
import logging
import warnings


class VlanTags(APIClassTemplate):
    """
    The VlanTags Object in the FMC.
    """

    URL_SUFFIX = '/object/vlantags'
    REQUIRED_FOR_POST = ['name', 'data']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for VlanTags class.")
        self.type = 'VlanTag'
        self.parse_kwargs(**kwargs)

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for VlanTags class.")
        if 'data' in kwargs:
            self.data = kwargs['data']

    def vlans(self, start_vlan, end_vlan=''):
        logging.debug("In vlans() for VlanTags class.")
        start_vlan, end_vlan = validate_vlans(start_vlan=start_vlan, end_vlan=end_vlan)
        self.data = {'startTag': start_vlan, 'endTag': end_vlan}


class VlanTag(VlanTags):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: VlanTag() should be called via VlanTags().")
        super().__init__(fmc, **kwargs)
