# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('commessa',pkey='id',name_long='Commessa',name_plural='Commesse',caption_field='id')
        self.sysFields(tbl)
        tbl.column('fasonista_id',size='22',name_long='Fasonista').relation('fasonista.id',relation_name='commesse', mode='foreignkey',deferred=True)
        tbl.column('codice_commessa',size=':13',name_long='Codice commessa',unique=True,indexed=True)
        tbl.column('codice_articolo',size=':18',name_long='Codice articolo'
                            ).relation('articolo.codice',
                                        relation_name='commesse',
                                        mode='foreignkey',deferred=True)
        tbl.column('data', dtype='D', name_long='Data')
        tbl.column('data_consegna', dtype='D', name_long='Data consegna')
        tbl.column('quantita', dtype='L', name_long='Quantità')


    def getCommessaDaRigaBollettina(self,riga=None):
        """
        ['codice_terzista', 'ragione_sociale', 'codice_destinazione', 
            'descrizione_destinazione', 'numero_bollettina',
             'data_bollettina', 'articolo',
              'descrizione_articolo', 'data_consegna', 
              'numero_pezzi_bollettina', 'numero_pezzi_da_produrre', 
              'priorita', 'flag_evasa', 'cod_tema', 'descrizione_tema',
               'codstagione', 'descrizione_stagione']
        
        """

    def onNewRecord(self,record):
        riga = record.pop('riga_importazione')
        record['data'] = self.normalizzaData(riga['data_bollettina'])
        record['data_consegna'] = self.normalizzaData(riga['data_consegna'])
        record['fasonista_id'] = self.db.table('lav.fasonista').insertIfMissing(
                    field='codice',field_value=riga['codice_terzista'],
                    nome=riga['ragione_sociale']
                )['id']
        record['codice_articolo'] = self.db.table('lav.articolo').insertIfMissing(
            field='codice',field_value=riga['articolo'],
            descrizione=riga['descrizione_articolo'],
            tema = riga['cod_tema'],
            tema_descrizione = riga['descrizione_tema'],
            stagione= riga['codstagione'],
            stagione_descrizione=riga['descrizione_stagione'],
            tipo = self.db.table('lav.articolo_tipo').sysRecord('PF')['codice']
            )['codice']
