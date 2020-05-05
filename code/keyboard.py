from vk_dev import Keyboard, Button


label = f"STOP!{' '*22}vto.pe"

menu =\
Keyboard(one_time=False).create(
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    Button.line(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    Button.line(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    Button.line(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).positive(),
    Button.text(payload="{}", label=label).negative(),
    Button.line(),
    Button.text(payload="{}", label=label).primary(),
    Button.text(payload="{}", label=label).positive(),
)
