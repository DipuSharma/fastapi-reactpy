from reactpy import component, html, web
import reactpy as rp
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
def childComponent():
    return html.div(
        Card({"maxWidth":"350px"},
            CardContent(
                Typography({
                    "variant": "h2",        
                    }, "Hello World"),
                    ),
            CardActions(
                Button({
                    "color":"primary",
                    "variant": "contained"
                            
                    }, "Submit Data")
                )
            )
        )