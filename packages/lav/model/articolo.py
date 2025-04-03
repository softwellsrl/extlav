# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('articolo', pkey='codice', name_long='Articolo', 
                            name_plural='Articoli',caption_field='descrizione')
        self.sysFields(tbl,id=False)
        tbl.column('codice', size=':18', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')
        tbl.column('tipo',size=':2', group='_', name_long='Tipo'
                    ).relation('articolo_tipo.codice', 
                                mode='foreignkey', onDelete='raise')
        tbl.column('tema',size=':2', group='_', name_long='Tema'
                    ).relation('articolo_tema.codice', mode='foreignkey', 
                            onDelete='raise')
        tbl.column('stagione',size=':3', group='_', name_long='Stagione'
                    ).relation('articolo_stagione.codice', mode='foreignkey', 
                    onDelete='raise')
        tbl.column('colore',size=':8', group='_', name_long='Colore'
                    ).relation('articolo_colore.codice', mode='foreignkey', 
                                onDelete='raise')


    def onNewRecord(self,record):
        self.db.table('lav.articolo_tema').insertIfMissing(
            field='codice',
            field_value=record['tema'],
            descrizione=record['tema_descrizione']
        )
        self.db.table('lav.articolo_stagione').insertIfMissing(
            field='codice',
            field_value=record['stagione'],
            descrizione=record['stagione_descrizione']
        )