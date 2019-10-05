#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Title      : PySMuRF Data Downsampler
#-----------------------------------------------------------------------------
# File       : __init__.py
# Created    : 2019-09-30
#-----------------------------------------------------------------------------
# Description:
#    SMuRF Data Downsampler Python Package
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
import pysmurf.core.common

class Downsampler(pysmurf.core.common.BaseMasterSlave):
    """
    SMuRF Data Downsampler Python Wrapper.
    """
    def __init__(self, name, **kwargs):
        self._downsampler = smurf.core.downsamplers.Downsampler()
        pysmurf.core.common.BaseMasterSlave.__init__(self, name=name, device=self._downsampler, description='SMuRF Data Downsampler', **kwargs)

        # Add the number of enabled channels  variable
        self.add(pyrogue.LocalVariable(
            name='NumChannels',
            description='Number of channels being processed',
            mode='RO',
            value=0,
            pollInterval=1,
            localGet=self._downsampler.getNumCh))

        # Add the filter order variable
        self.add(pyrogue.LocalVariable(
            name='Factor',
            description='Downsampling factor',
            mode='RW',
            value=1,
            localSet=lambda value : self._downsampler.setFactor(value),
            localGet=self._downsampler.getFactor))

