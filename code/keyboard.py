from vk_dev import keyboard, Button


label = f"STOP!{' '*22}vto.pe"

menu =\
keyboard(one_time=False).create(
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    button.line(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).secondary(),
    button.line(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).secondary(),
    button.line(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).secondary(),
)
