### GuiElement - Identification and Interactions

A single HTML node in the DOM of a web UI is represented by a GuiElement object in Arjuna, irrespective of its type. This is unless you need specialized methods which we will see later.

Arjuna supports the locators which are supported by Selenium's By object. Apart from these, there are various abstracted locators which Arjuna provides for easier coding.

The locator strategy is expressed by using various factory methods of Arjuna's **`With`** class.

For this section, we'll use the login page of WordPress CMS. The elements of interest are the **User Name** field and the **Lost Your Password?** link.

<img src="img/wp_login.png" height="500" width="500">

In the above page, the HTML for the **User Name** field is:

```html
<input type="text" name="log" id="user_login" class="input" value="" size="20">
```

and for **Lost Your Password?** link is:

```html
<a href="/wp-login.php?action=lostpassword" title="Password Lost and Found">Lost your password?</a>
```

#### Identification using ID, Name, Class Name, Tag Name, Link Text, Partial Link Text

```python
# arjuna-samples/arjex_webui_basics/tests/modules/test_02_guielement.py

@test
def test_basic_identifiers(my, request):
    wp_url = Arjuna.get_ref_config().get_user_option_value("wp.login.url").as_str()
    wordpress = WebApp(base_url=wp_url)
    wordpress.launch()

    # user name field.
    # Html of user name: 
    element = wordpress.ui.element(With.id("user_login"))
    element = wordpress.ui.element(With.name("log"))
    element = wordpress.ui.element(With.class_name("input"))
    element = wordpress.ui.element(With.tag_name("input"))

    # Lost your password link
    # Html of link: 
    element = wordpress.ui.element(With.link_text("Lost your password?"))
    element = wordpress.ui.element(With.link_ptext("password"))

    wordpress.quit()
```

##### Points to Note
1. Launch the WebApp. Use a WordPress deployment of choice. For example code creation, a VirtualBox image of Bitnami Wordpress was used.
2. GuiElement identification if done by calling the **`element`** factory method of `ui` object of `WebApp`.
3. The locator strategy is expressed using factory methods of **`With`** class which correspond as follows:
    - **`With.id`** - ID attribute
    - **`With.name`** - Name attribute
    - **`With.class_name`** - One of the class names in class attribute
    - **`With.tag_name`** - Tag Name
    - **`With.link_text`**  - Link Text
    - **`With.link_ptext`** - A part of Link's text
4. Quit the app using its `quit` method.