from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, hooks
import reactpy as rp


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
    
def increment(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


@component
def MainComponent():
    return html.div(Counter1(), Counter2())   # Multiple component add under main component

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
@component 
def Counter2():           # Component 2nd
    initial_count = 0
    count, set_count = hooks.use_state(initial_count)
    return html.div(
        html.h1(html.span('Using Use State ')),
        html.h1(f"Count: {count}"),
        html.br(),
        html.button(
            {"on_click": lambda event: set_count(initial_count)}, "Reset"
        ),
        html.button({"on_click": lambda event: set_count(increment)}, "+"),
        html.button({"on_click": lambda event: set_count(decrement)}, "-"),
    )
app = FastAPI()
configure(app, MainComponent)