# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.thpage("Commesse", table="lav.commessa")
        root.thpage("Fasonisti", table="lav.fasonista")
        root.thpage("Piani lavorazione", table="lav.piano_lavorazione")
        root.thpage("Articolo", table="lav.articolo")
        root.lookupBranch("!!Tabelle", pkg="lav")

