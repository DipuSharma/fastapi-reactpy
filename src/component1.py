from reactpy import component, html, hooks

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
        html.h1(html.span('Using Supplimentry Hooks')),
        html.h1(f"Count: {count}"),
        html.br(),
        html.button({"on_click": lambda event: dispatch("reset")}, "Reset"),
        html.button({"on_click": lambda event: dispatch("increment")}, "+"),
        html.button({"on_click": lambda event: dispatch("decrement")}, "-"),
    )