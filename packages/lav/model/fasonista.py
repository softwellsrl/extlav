# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('fasonista',pkey='id',name_long='Fasonista',
                name_plural='Fasonisti',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('codice',size=':5',name_long='Codice',unique=True)
        tbl.column('nome',size=':50',name_long='Nome')


    def getFasonistaDaRigaBollettina(self,riga):
        pass