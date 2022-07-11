from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class ContactApphook(CMSApp):
    app_name = "contact"
    name = "Contact Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["contact.urls"]