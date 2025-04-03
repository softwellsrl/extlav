# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.h1('Lavorazioni',text_align='center')
        root.button('logout',action='genro.logout()')
