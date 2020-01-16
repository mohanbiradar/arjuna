'''
Testers use 3 approaches for Dropdown controls in web test automation using Selenium.
1. Using Selenium's Select class as it provides higher level methods.
2. Using sendKeys() method of WebElement.
3. (Especially for custom select controls) - Click the drop down control and then click the option. 

Arjuna tries to cater to all of them with a single abstraction - its DropDown object.

3 will be covered later when element configuration has been discussed.
'''

from arjuna.tpi import Arjuna
from arjuna.tpi.guiauto.helpers import With

from commons import *

init_arjuna()
automator = launch_automator()
login(automator)

automator.element(With.link_text("Settings")).click()

role_select = automator.dropdown(With.id("default_role"))
role_select.select_value("editor")

role_select.select_visible_text("Subscriber")
print(role_select.has_visible_text_selected("Subscriber"))
print(role_select.has_value_selected("subscriber"))
print(role_select.has_index_selected(2))
print(role_select.first_selected_option_value)
print(role_select.first_selected_option_text)

role_select.select_index(4)
print(role_select.has_index_selected(4))

text = "Subscriber"

role_select.send_option_text(text)
assert role_select.has_visible_text_selected("Subscriber") is True

logout(automator)