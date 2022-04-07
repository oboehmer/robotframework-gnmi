
from robot.api.deco import keyword
from robot.api import logger
from pygnmi.client import gNMIclient


class GNMI(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.sessions = {}

    @keyword('GNMI connect session')
    def connect_session(self, session, timeout=None, **kwargs):
        if not session:
            raise ValueError('need to provide a non-empty session parameter')
        if session in self.sessions:
            raise ValueError('Session {} is already connected'.format(session))

        # TODO: for now just pass all kwargs into gNMIclient, reckon we want to
        # expose a few of the kwargs as reqired args, not sure what is required
        logger.debug('Starting new session {} with args {}'.format(
            session,
            ', '.join('{}={}'.format(k, v) for k, v in kwargs.items())
        ))
        self.sessions['session'] = gNMIclient(**kwargs)
        self.sessions['session'].connect(timeout=timeout)

    @keyword('GNMI get')
    def get(self, session, prefix: str = "", path: list = [], datatype: str = 'all', encoding: str = 'json'):

        if not (session and session in self.sessions):
            raise ValueError('Session {} is not established, please connect it first'.format(session))
        return self.sessions[session].get(prefix=prefix, path=path, datatype=datatype, encoding=encoding)

    @keyword('GNMI set')
    def set_(self, session, delete: list = None, replace: list = None, update: list = None, encoding: str = 'json'):

        if not (session and session in self.sessions):
            raise ValueError('Session {} is not established, please connect it first'.format(session))

        return self.sessions[session].set(delete=delete, replace=replace, update=update, encoding=encoding)
