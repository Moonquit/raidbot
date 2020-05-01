from vk_api.keyboard import VkKeyboard

label = f"STOP!{' '*22}vto.pe"

menu = VkKeyboard()
one_time = False

#1 line (2 buttons)
menu.add_button(
    label=label,
    color="positive"
)
menu.add_button(
    label=label,
    color="negative"
)

menu.add_line()


#2 line (4 buttons)
menu.add_button(
    label=label,
    color="primary")

menu.add_button(
    label=label,
    color="positive")


menu.add_button(
    label=label,
    color="positive"
)
menu.add_button(
    label=label,
    color="negative"
)

menu.add_line()


#3 line (4 buttons)
menu.add_button(
    label=label,
    color="primary")

menu.add_button(
    label=label,
    color="positive")


menu.add_button(
    label=label,
    color="positive"
)
menu.add_button(
    label=label,
    color="negative"
)

menu.add_line()


#4 line (4 buttons)
menu.add_button(
    label=label",
    color="primary")

menu.add_button(
    label=label,
    color="positive")


menu.add_button(
    label=label,
    color="positive"
)
menu.add_button(
    label=label,
    color="negative"
)

menu.add_line()


# 5 line (2 buttons)
menu.add_button(
    label=label,
    color="primary")

menu.add_button(
    label=label,
    color="positive")

menu = menu.get_keyboard()
