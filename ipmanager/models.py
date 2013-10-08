from django.db import models
from django.core.validators import validate_ipv46_address
from django.core.exceptions import ValidationError
import re

def mac_address_validator(mac):
    if not re.match(r'^[0-9a-fA-F]{12}$', mac):
        raise ValidationError("Incorrect MAC address")

class Host(models.Model):
    mac = models.CharField('MAC', max_length=12, validators=[mac_address_validator])
    ip = models.CharField('IP', max_length=45, validators=[validate_ipv46_address])
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s:%s" % (self.mac, self.ip)


