# _*_ coding: utf-8 _*_

"""
proxies.py by xianhu
"""

import logging
from .base import TPEnum, BaseThread


class ProxiesThread(BaseThread):
    """
    class of ProxiesThread, as the subclass of BaseThread
    """

    def working(self):
        """
        procedure of proxies, auto running, and return False if you need stop thread
        """
        # ----2----
        proxies_state, proxies_result = self._worker.working()

        # ----3----
        if proxies_state > 0:
            for proxies in proxies_result:
                self._pool.add_a_task(TPEnum.PROXIES, proxies)
        else:
            logging.error("%s error: %s", proxies_result[0], proxies_result[1])

        # ----5----
        return not (self._pool.is_all_tasks_done() and self._pool.get_thread_stop_flag())
