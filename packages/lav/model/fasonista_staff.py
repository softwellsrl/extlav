# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('fasonista_staff', pkey='id', name_long='Staff', name_plural='Staff',caption_field='nome')
        self.sysFields(tbl,counter='fasonista_id')
        tbl.column('fasonista_id',size='22', group='_', name_long='Fasonista'
                    ).relation('fasonista.id', relation_name='staff', 
                                    mode='foreignkey', onDelete='cascade')
        tbl.column('nome', name_long='Nome')
        tbl.column('cognome', name_long='Cognome')
        tbl.column('email', name_long='Email')
        tbl.column('user_group',size=':15', group='_', name_long='Gruppo'
                    ).relation('adm.group.code', mode='foreignkey', onDelete='raise')


    def creaUtente(self,staff_id=None):
        record = self.record(staff_id).output('dict')
        usertbl = self.db.table('adm.user')
        with usertbl.recordToUpdate(fasonista_staff_id=staff_id,
                                    insertMissing=True,assignId=True) as user_record:
            user_record.update(dict(fasonista_staff_id=staff_id,
                            email=record['email'],
                            firstname=record['nome'],
                            lastname=record['cognome'],
                            username=record['email'],
                            group_code=record['user_group'],
                            status='new'))
        return user_record['id']
