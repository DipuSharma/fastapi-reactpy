from reactpy import component, html, hooks, web

mui = web.module_from_template(
    "react",
    "@mui/material",
    fallback="please wait loading ......."
)
Conatiner = web.export(mui, "Container")
Stack = web.export(mui, "Stack")
Button = web.export(mui, "Button")
Card = web.export(mui, "Card")
CardContent = web.export(mui, 'CardContent')
CardActions = web.export(mui, "CardActions")
Alert = web.export(mui, "Alert")
Typography = web.export(mui, "Typography")


def reducer(count, action):
    if action == "increment":
        return count + 1
    elif action == "decrement":
        return count - 1
    elif action == "reset":
        return 0
    else:
        msg = f"Unknown action '{action}'"
        raise ValueError(msg)


@component
def Counter1():           # Component 1st
    count, dispatch = hooks.use_reducer(reducer, 0)
    return html.div(
        Conatiner(
        {"style": {"width": "100%", "background-color":"red", "padding-bottom":"10px"}},
        html.h1(html.span('Using Hooks')),
        html.h1({"style": {"color":"white"}},f"Count: {count}"),
        html.br(),
        Stack(
            {"direction":"row", "spacing":f"{2}"},
            Button({"color": "primary", "variant": "contained",
               "on_click": lambda event: dispatch("increment")}, "+"),
            Button({"color": "primary", "variant": "contained",
                "on_click": lambda event: dispatch("decrement")}, "-"),
            Button({"color": "warning", "variant": "contained",
                "on_click": lambda event: dispatch("reset")}, "Reset"),
            )
        )
    )
