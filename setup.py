from DistUtilsExtra.auto import setup
from distutils.command.install import install
import os

PACKAGE="ticket-to-pdf"
VERSION="1.0"

# In case we need hooks
class post_install(install):
    def run(self):
        install.run(self)

setup(
    name              = PACKAGE,
    author            = "CPAC Applications",
    author_email      = "cpac@ao-cs.com",
    url               = "http://www.cpac.com",
    version           = VERSION,
    packages          = [ "ticket-to-pdf" ],
    license           = "Copyright 2021, CPAC Equipment Inc.",
    description       = "Produces a pdf of an RHPro ticket file",
    long_description  = open("README.md").read(),
    cmdclass          = { 'install': post_install },
    data_files        = [('/usr/bin', [
                            'ticket-to-pdf/ticket-to-pdf',
                        ])],
)
