from reactpy import component, hooks, html
from src.component1 import Button, Conatiner


def increment(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


@component
def Counter2():           # Component 2nd
    initial_count = 0
    count, set_count = hooks.use_state(initial_count)
    return html.div(Conatiner(
        {"style": {"width": "100%", "color":"white","background-color":"black", "padding-bottom":"10px"}},
        html.h1(html.span('Using State ')),
        html.h1(f"Count: {count}"),
        html.br(),
        # html.button(
        #     {"on_click": lambda event: set_count(initial_count)}, "Reset"
        # ),
        # html.button({"on_click": lambda event: set_count(increment)}, "+"),
        # html.button({"on_click": lambda event: set_count(decrement)}, "-"),

        Button({"color": "warning", "variant": "contained",
               "on_click": lambda event: set_count(initial_count)}, "Reset"),
        Button({"color": "primary", "variant": "contained",
               "on_click": lambda event: set_count(increment)}, "+"),
        Button({"color": "primary", "variant": "contained",
               "on_click": lambda event: set_count(decrement)}, "-"),
    )
    )
