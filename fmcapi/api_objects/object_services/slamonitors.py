from fmcapi.api_objects.apiclasstemplate import APIClassTemplate
from .securityzones import SecurityZones
import logging
import warnings


class SLAMonitors(APIClassTemplate):
    """
    The SLAMonitors Object in the FMC.
    """
    URL_SUFFIX = '/object/slamonitors'
    REQUIRED_FOR_POST = ['name', 'slaId', 'monitorAddress', 'interfaceObjects', 'type']
    REQUIRED_FOR_PUT = ['id', 'type']

    def __init__(self, fmc, **kwargs):
        super().__init__(fmc, **kwargs)
        logging.debug("In __init__() for SLAMonitors class.")
        self.parse_kwargs(**kwargs)
        self.type = "SLAMonitor"

    def parse_kwargs(self, **kwargs):
        super().parse_kwargs(**kwargs)
        logging.debug("In parse_kwargs() for SLAMonitors class.")
        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
        if 'threshold' in kwargs:
            self.securityZone = kwargs['threshold']
        if 'frequency' in kwargs:
            self.frequency = kwargs['frequency']
        if 'slaId' in kwargs:
            self.slaId = kwargs['slaId']
        if 'dataSize' in kwargs:
            self.dataSize = kwargs['dataSize']
        if 'tos' in kwargs:
            self.tos = kwargs['tos']
        if 'noOfPackets' in kwargs:
            self.noOfPackets = kwargs['noOfPackets']
        if 'monitorAddress' in kwargs:
            self.monitorAddress = kwargs['monitorAddress']
        if 'interfaceObjects' in kwargs:
            self.interfaceObjects = kwargs['interfaceObjects']
        if 'description' in kwargs:
            self.description = kwargs['description']

    def interfaces(self, names):
        logging.debug("In interfaces() for SLAMonitors class.")
        zones = []
        for name in names:
            # Supports passing list of str
            sz = SecurityZones(fmc=self.fmc)
            sz.get(name=name)
            if 'id' in sz.__dict__:
                zones.append({'name': sz.name, 'id': sz.id, 'type': sz.type})
            else:
                logging.warning(f'Security Zone, "{name}", not found.  Cannot add to SLAMonitors.')
        if len(zones) != 0:
            # Make sure we found at least one zone
            self.interfaceObjects = zones
        else:
            logging.warning(f'No valid Security Zones found: "{names}".  Cannot add to SLAMonitosr.')


class SLAMonitor(SLAMonitors):
    """Dispose of this Class after 20210101."""

    def __init__(self, fmc, **kwargs):
        warnings.resetwarnings()
        warnings.warn("Deprecated: SLAMonitor() should be called via SLAMonitors().")
        super().__init__(fmc, **kwargs)
