# encoding: utf-8
from gnr.core.gnrdecorator import metadata


class Table(object):
    @metadata(mandatory=True)
    def sysRecord_FAS_STAFF(self):
        return self.newrecord(code='FAS_STAFF',
                                description='Staff fasonista',
                                rootpage='/lav/lavorazioni')   


    @metadata(mandatory=True)
    def sysRecord_FAS_ADMIN(self):
        return self.newrecord(code='FAS_ADMIN',description='Admin fasonista')   


    @metadata(mandatory=True)
    def sysRecord_PRD_ADMIN(self):
        return self.newrecord(code='PRD_ADMIN',description='Prd admin')   



    @metadata(mandatory=True)
    def sysRecord_PRD_STAFF(self):
        return self.newrecord(code='PRD_STAFF',description='Prd staff',
                                 rootpage='/lav/gestione')   



    @metadata(mandatory=True)
    def sysRecord_WSAI(self):
        return self.newrecord(code='WSAI',description='WSAI')   

