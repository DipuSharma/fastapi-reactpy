from reactpy import component, hooks, html, web
from main import sculpture_data

mui = web.module_from_template(
    "react",
    "@mui/material",
    fallback="please wait loading ......."
)
Container = web.export(mui, "Container")
Row = web.export(mui, "Row")
Button = web.export(mui, "Button")
Card = web.export(mui, "Card")
CardContent = web.export(mui, 'CardContent')
CardActions = web.export(mui, "CardActions")
Alert = web.export(mui, "Alert")
Typography = web.export(mui, "Typography")

@component
def Gallery():
    index, set_index = hooks.use_state(0)
    def prev_image(event):
        set_index(index - 1)
    def next_image(event):
        set_index(index + 1)

    bounded_index = index % len(sculpture_data)
    sculpture = sculpture_data[bounded_index]
    alt = sculpture["alt"]
    artist = sculpture["artist"]
    description = sculpture["description"]
    name = sculpture["name"]
    url = sculpture["url"]

    
    return Container(
        html.div(
        Button({"color":"success","variant": "contained","on_click": prev_image}, "Prev"),
        Button({"color":"error","variant": "contained","on_click": next_image}, "Next"),
        html.h2(name, " by ", artist),
        html.p({"style":{"font-size":"25px", "font-weight":"bold"}},f"({bounded_index + 1} of {len(sculpture_data)})"),
        html.img({"src": url, "alt": alt, "style": {"height": "250px", "width": "200px"}}),
        html.p({"style":{"font-size":"15px"}},f"{description}"),
    )
    )