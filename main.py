from flet import *

def main(page: Page):
    page.title = "My App"
    page.window.width=390
    page.window.height = 740

    # باقي عناصر واجهة المستخدم
    page.update()
app(target=main,assets_dir="assets")
