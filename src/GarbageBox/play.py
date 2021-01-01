import sys
from playwright.sync_api import Page


class TestPlanisphere:
    def test_reserve_otoku(self, page: Page):
        page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0")
        page.waitForLoadState("networkidle")

        page.close()