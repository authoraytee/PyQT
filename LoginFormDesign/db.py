import re

accounts = {
    "alex@gmail.com": "sasha228",
    "someone@gmail.com": "password1122",
    "anybody@gmail.com": "newpass121212",
    "pudgess@gmail.com": "mid",
}

def get_output(login, passwd):
    try:
        if accounts[login] == passwd:
            output = "Thanks for loging!"
        else:
            output = "Password or login are incorrect!"
    except:
        email_regex = r'\b[\w.-]+?@\w+?\.\w+?\b'
        valid_form = re.findall(email_regex,login)

        if not valid_form:
            output = "Login form is invalid"
        elif valid_form:
            output = "Password or login are incorrect!"
        else:
            output = ""

    return output