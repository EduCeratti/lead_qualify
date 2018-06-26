from django.db import models

# Create your models here.
class Touchpoint(models.Model):            
    
    IMPORTED = 'IM'
    QUALIFIED = 'QL'
    DISTRIBUTED = 'DI'
    
    TOUCHPOINT_STATUS = (
        (IMPORTED, 'Imported'),
        (QUALIFIED, 'Qualified'),
        (DISTRIBUTED, 'Distributed'),
    )

    NA = 0
    APPROVED = 1
    REPROVED = 2
    
    RULE_APPROVED = (
        (NA, 'Not available'),
        (APPROVED, 'Approved'),
        (REPROVED, 'Reproved'),
    )
    
    username = models.CharField(max_length=100)
    modified_date = models.DateField()
    rule_approved = models.IntegerField(choices=RULE_APPROVED, default=NA)
    status = models.CharField(
        max_length=2,
        choices=TOUCHPOINT_STATUS,
        default=IMPORTED,
    )