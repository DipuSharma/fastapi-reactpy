from reactpy import component, html, web
from src.component1 import Counter1
from src.component2 import Counter2
from page import childComponent


mui = web.module_from_template(
    "react",
    "@mui/material",
    fallback="please wait loading ......."
)

Button = web.export(mui, "Button")
Card = web.export(mui, "Card")
CardContent = web.export(mui, 'CardContent')
CardActions = web.export(mui, "CardActions")
Alert = web.export(mui, "Alert")
Typography = web.export(mui, "Typography")


  # Multiple component add under main component
@component
def MainComponent():
    return html.div(
        Button({"color":"primary", "variant":"contained"}, "Button1"),
        Button({"color":"warning", "variant":"contained"}, "Button2"),
        Counter1(), Counter2(), childComponent()
        
        ) 