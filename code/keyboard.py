from vk_api.keyboard import VkKeyboard

label = f"STOP!{' '*22}vto.pe"

menu = VkKeyboard()
menu.add_button(
    label=label,
    color="positive"
)
menu.add_button(
    label=label,
    color="negative"
)

menu.add_line()
menu.add_button(
    label=label,
    color="primary"
)

menu.add_button(
    label=label,
    color="positive"
)

menu = menu.get_keyboard()
