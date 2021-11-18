from features.support.enviroments.EnvStg import EnvStg
from features.support.enviroments.EnvPrd import EnvPrd
from features.utils import constants, logger


class SetEnvironments(object):
    def __init__(self, enviroment):
        match enviroment:
            case 'STG':
                EnvStg()
            case 'PRD':
                EnvPrd()
            case _:
                logger.logging.info(constants.AMBIENTE_NAO_ENCONTRADO % enviroment)
