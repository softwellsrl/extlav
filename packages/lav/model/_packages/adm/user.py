# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('user')
        tbl.column('fasonista_staff_id',size='22', group='_', name_long='Staff fasonista'
                    ).relation('lav.fasonista_staff.id',one_one='*', mode='foreignkey', onDelete='raise')        