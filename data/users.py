"""Public demo credentials published on the SauceDemo login page."""
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str = 'secret_sauce'


STANDARD = User('standard_user')
LOCKED_OUT = User('locked_out_user')
PROBLEM = User('problem_user')
PERFORMANCE_GLITCH = User('performance_glitch_user')


class Messages:
    LOCKED_OUT = 'Epic sadface: Sorry, this user has been locked out.'
    USERNAME_REQUIRED = 'Epic sadface: Username is required'
    PASSWORD_REQUIRED = 'Epic sadface: Password is required'
    INVALID_CREDENTIALS = 'Epic sadface: Username and password do not match any user in this service'
    FIRST_NAME_REQUIRED = 'Error: First Name is required'
    ORDER_COMPLETE = 'Thank you for your order!'
