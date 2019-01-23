import attr
import time

from usmqe.base.application.entities import BaseCollection, BaseEntity
from usmqe.base.application.implementations.web_ui import ViaWebUI


@attr.s
class Brick(BaseEntity):
    brick_path = attr.ib()
    hostname = attr.ib()
    volume_name = attr.ib()
    utilization = attr.ib()
    disk_device_path = attr.ib()
    port = attr.ib()

    def view_dashboard():
        pass


@attr.s
class HostBricksCollection(BaseCollection):
    ENTITY = Brick

    def get_bricks(self):
        view = ViaWebUI.navigate_to(self.parent, "Bricks")
        time.sleep(4)
        brick_list = []
        for row in view.bricks:
            brick = self.instantiate(
                row[0].text,
                view.hostname.text,
                row[1].text,
                row[2].text,
                row[3].text,
                row[4].text)
            brick_list.append(brick)
        return brick_list
