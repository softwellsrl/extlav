# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Menu(object):
    def config(self,root,**kwargs):
        root.thpage("Commesse", table="lav.commessa")
        root.thpage("Fasonisti", table="lav.fasonista")
        root.thpage("Piani lavorazione", table="lav.piano_lavorazione",tags='grp_PRD_ADMIN')
        root.thpage("Articolo", table="lav.articolo")
        root.lookupBranch("!!Tabelle", pkg="lav")


class ApplicationMenu(object):


    def config(self,root,**kwargs):
        root.packageBranch('Sistema',pkg='sys',tags='_DEV_,grp_WSAI')
        root.packageBranch('Utenti e gruppi',pkg='adm',tags='_DEV_,grp_WSAI')
        root.packageBranch('Gestione lavorazioni',pkg='lav')


    @metadata(group_code='FAS_ADMIN')
    def config_amministratoreFasonista(self,root,**kwargs):
        root.thpage("Commesse", table="lav.commessa")
        root.thpage('Profilo',table='lav.fasonista',
                        formResource='FormProfilo',
                        url_pkey=self.db.currentEnv['fasonista_id'])
        root.thpage("Piani lavorazione", table="lav.piano_lavorazione")
