from gnr.web.gnrbaseclasses import BaseComponent

class LoginComponent(BaseComponent):

    def onAuthenticating_lav(self,avatar,rootenv=None):
        if avatar.authmode=='xml':
            return
        rootenv['fasonista_id'] = self.db.table('adm.user').readColumns(
            pkey=avatar.user_id,
            columns='@fasonista_staff_id.fasonista_id'
        )
        rootenv['current_fasonista_id'] = rootenv['fasonista_id']