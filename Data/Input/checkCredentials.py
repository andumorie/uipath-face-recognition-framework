
import win32security
import win32api


def checkCredentials(user, passw, should_check):
    if not should_check:
        return 'Success'
    domain, username = win32api.GetUserNameEx(win32api.NameSamCompatible).split('\\')
    if user.lower() != username.lower():
        return 'Wrong credentials. Please try again.'
    try:
        lg = win32security.LogonUser(user, domain, passw, win32security.LOGON32_LOGON_NETWORK,win32security.LOGON32_PROVIDER_DEFAULT)
    except:
        return 'Wrong credentials. Please try again.'
    else:
        return 'Success'
