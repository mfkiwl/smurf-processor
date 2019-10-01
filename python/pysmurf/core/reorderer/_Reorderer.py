#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : PySMuRF Data Re-orderer
#-----------------------------------------------------------------------------
# File       : __init__.py
# Created    : 2019-09-30
#-----------------------------------------------------------------------------
# Description:
#    SMuRF Data Re-orderer Python Package
#-----------------------------------------------------------------------------
# This file is part of the smurf software platform. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the smurf software platform, including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import pyrogue
import smurf

class Reorderer(pyrogue.Device):
    """
    SMuRF Data Re-orderer Python Wrapper.
    """
    def __init__(self, name, **kwargs):
        pyrogue.Device.__init__(self, name=name, description='SMuRF Data Re-orderer', **kwargs)
        self._reorderer = smurf.core.reorderer.Reorderer()

        # Add "Disable" variable
        self.add(pyrogue.LocalVariable( name='Disable',
                                        description='Disable the processing block. Data will just pass thorough to the next slave.',
                                        mode='RW',
                                        pollInterval=1,
                                        value=False,
                                        locaSet=self._reorderer.getDisable,
                                        localGet=self._reorderer.setDisable))

    # Method called by streamConnect, streamTap and streamConnectBiDir to access slave
    def _getStreamSlave(self):
        return self._reorderer

    # Method called by streamConnect, streamTap and streamConnectBiDir to access master
    def _getStreamMaster(self):
        return self._reorderer