
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

        if 'debug' not in kwargs:
            kwargs['debug'] = True

        # TODO: for now just pass all kwargs into gNMIclient, reckon we want to
        # expose a few of the kwargs as reqired args, not sure what is required
        logger.debug('Starting new session {} with args {}'.format(
            session,
            ', '.join('{}={}'.format(k, v) for k, v in kwargs.items())
        ))
        self.sessions[session] = gNMIclient(**kwargs)
        self.sessions[session].connect(timeout=timeout)

    @keyword('GNMI get')
    def get(self, session, prefix: str = "", path: list = [], datatype: str = 'all', encoding: str = 'json'):
        """
        Collecting the information about the resources from defined paths.

        Path is provided as a list in the following format:
          path = ['yang-module:container/container[key=value]', 'yang-module:container/container[key=value]', ..]
        Available path formats:
          - yang-module:container/container[key=value]
          - /yang-module:container/container[key=value]
          - /yang-module:/container/container[key=value]
          - /container/container[key=value]
          - /
        The datatype argument may have the following values per gNMI specification:
          - all
          - config
          - state
          - operational
        The encoding argument may have the following values per gNMI specification:
          - json
          - bytes
          - proto
          - ascii
          - json_ietf
        """
        if not (session and session in self.sessions):
            raise ValueError('Session {} is not established, please connect it first'.format(session))
        result = self.sessions[session].get(prefix=prefix, path=path, datatype=datatype, encoding=encoding)
        logger.info('get() call returned: {}'.format(result))

        if result is None:
            raise Exception('Error retrieving data, please check logs for detail')

        return result

    @keyword('GNMI set')
    def set_(self, session, delete: list = None, replace: list = None, update: list = None, encoding: str = 'json'):
        """
        Changing the configuration on the destination network elements.
        Could provide a single attribute or multiple attributes.
        delete:
          - list of paths with the resources to delete. The format is the same as for get() request
        replace:
          - list of tuples where the first entry path provided as a string, and the second entry
            is a dictionary with the configuration to be configured
        replace:
          - list of tuples where the first entry path provided as a string, and the second entry
            is a dictionary with the configuration to be configured
        The encoding argument may have the following values per gNMI specification:
          - json
          - bytes
          - proto
          - ascii
          - json_ietf
        """

        if not (session and session in self.sessions):
            raise ValueError('Session {} is not established, please connect it first'.format(session))

        result = self.sessions[session].set(delete=delete, replace=replace, update=update, encoding=encoding)
        logger.info('set() call returned: {}'.format(result))

        if result is None:
            raise Exception('Error executing set operation, please check logs for detail')

        return result
