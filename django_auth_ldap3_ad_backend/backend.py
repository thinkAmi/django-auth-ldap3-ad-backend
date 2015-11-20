from django.contrib.auth import get_user_model
from django.conf import settings
from ldap3 import Server, Connection, NTLM

class ADBackend(object):
    def authenticate(self, username=None, password=None):
        server = Server(settings.AD_DOAMIN_CONTROLLER_HOST_NAME)

        try:
            # auto_bindありのConnectionの生成で例外が発生しなければ、認証成功とみなす
            c = Connection(server,
                           user="{0}\\{1}".format(settings.AD_DOMAIN_NAME, username),
                           password=password,
                           authentication=NTLM,
                           auto_bind=True)
            user = get_user_model()

            result, created = user.objects.update_or_create(
                username = username,
                password = password
            )
            c.unbind()
            return result

        except:
            return None

    def get_user(self, user_id):
        user = get_user_model()
        try:
            return user.objects.get(pk=user_id)
        except:
            return None
