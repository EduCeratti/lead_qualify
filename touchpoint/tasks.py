from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.decorators import periodic_task
from celery.task.schedules import crontab

from touchpoint.import_lead import do_import
from touchpoint.qualify_lead import do_qualify

logger = get_task_logger(__name__)

# Periodic task to import leads - Every 2 minutes
@periodic_task(
    run_every=(crontab(minute='*/2')),
    name="import_lead_periodic_task",
    ignore_result=True
)
def import_lead_task():
    """ Import an lead if already not exists """
    logger.info("Making lead importation...")
    return do_import()

# Periodic task to import leads - Every 1 minute
@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="qualify_lead_periodic_task",
    ignore_result=True
)
def qualify_lead_task():
    """ Qualify all imported tasks """
    logger.info("Making lead qualify...")
    return do_qualify()