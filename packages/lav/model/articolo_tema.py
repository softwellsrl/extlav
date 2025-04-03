# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('articolo_tema', pkey='codice', name_long='Tema', name_plural='Temi',caption_field='descrizione',lookup=True)
        self.sysFields(tbl,counter=True,id=False)
        tbl.column('codice', size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')
