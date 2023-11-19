from app import app


@app.route('/sign_up')
def sign_up():
    """
    View function to handle sign up functionality so as to save user information
    """
    return ("Sign up Page")


@app.route('/sign_in')
def sign_in():
    """
    View function to handle sign in functionality so as to load user information
    """
    return ("Sign in Page")


@app.route('/sign_out')
def sign_out():
    """
    View function to handle sign out functionality
    """
    return ("Sign out Page")
