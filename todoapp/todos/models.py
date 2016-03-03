from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _


class ToDo(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    done = models.BooleanField(_("Done"), default=False)

    def __unicode__(self):
        return smart_unicode(self.name)
