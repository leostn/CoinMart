import threading
from selenium import webdriver
import flaskr
from flaskr import app


def before_all(ctx):
    ctx.server = flaskr
    ctx.thread = threading.Thread(target=ctx.server.test_server)
    ctx.thread.start()  # start flask app server
    ctx.browser = webdriver.Chrome()
    ctx.server_address = "http://" + app.config['SERVER_NAME']
    ctx.home = ctx.server_address


def after_all(ctx):
    ctx.browser.get(ctx.server_address + "/shutdown")# shut down flask app server
    ctx.thread.join()
    ctx.browser.quit()

