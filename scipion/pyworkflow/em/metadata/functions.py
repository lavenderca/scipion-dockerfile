# **************************************************************************
# *
# * Authors:     J.M. De la Rosa Trevin (jmdelarosa@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************
"""
Add functions related to metadata
"""
import xmipp

getBlocksInMetaDataFile = xmipp.getBlocksInMetaDataFile

label2Str = xmipp.label2Str 

colorStr = xmipp.colorStr 

labelType = xmipp.labelType 

labelHasTag = xmipp.labelHasTag 

labelIsImage = xmipp.labelIsImage 

str2Label = xmipp.str2Label 

isValidLabel = xmipp.isValidLabel

MDValueRelational = xmipp.MDValueRelational

MDValueEQ = xmipp.MDValueEQ 

MDValueNE = xmipp.MDValueNE 

MDValueLT = xmipp.MDValueLT 

MDValueLE = xmipp.MDValueLE 

MDValueGT = xmipp.MDValueGT 

MDValueGE = xmipp.MDValueGE 

MDValueRange = xmipp.MDValueRange 

addLabelAlias = xmipp.addLabelAlias

activateMathExtensions = xmipp.activateMathExtensions

getSymmetryMatrices = xmipp.SymList().getSymmetryMatrices