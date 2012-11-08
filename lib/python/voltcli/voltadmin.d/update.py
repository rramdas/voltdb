# This file is part of VoltDB.

# Copyright (C) 2008-2012 VoltDB Inc.
#
# This file contains original code and/or modifications of original code.
# Any modifications made by VoltDB Inc. are licensed under the following
# terms and conditions:
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from voltcli import utility

@VOLT.Command(
    wrapper = VOLT.AdminWrapper(),
    description = 'Update the schema of a running database.',
    arguments = (
        VOLT.StringArgument('catalog', 'the new application catalog jar file path'),
        VOLT.StringArgument('deployment', 'the deployment configuration file path')
    )
)
def update(runner):
    columns    = [VOLT.FastSerializer.VOLTTYPE_STRING, VOLT.FastSerializer.VOLTTYPE_STRING]
    catalog    = VOLT.utility.File(runner.opts.catalog).read_hex()
    deployment = VOLT.utility.File(runner.opts.deployment).read()
    params     = [catalog, deployment]
    # call_proc() aborts with an error if the update failed.
    runner.call_proc('@UpdateApplicationCatalog', columns, params)
    utility.info('The catalog update succeeded.')
