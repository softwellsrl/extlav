# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('articolo_colore', pkey='codice', 
                            name_long='Colore articolo', 
                        name_plural='Colori articoli',
                        caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False,counter=True)
        tbl.column('codice', size=':8', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')
        