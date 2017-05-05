def login(ctx, username='admin', password='Admin123'):
    ctx.browser.get(ctx.server_address + "/login")
    uname = ctx.browser.find_element_by_name('username')
    passwd = ctx.browser.find_element_by_name('password')
    login_button = ctx.browser.find_element_by_name('login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()

def logout(ctx):
    pass