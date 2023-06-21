from reactpy import component, html
from src.component1 import Counter1
from src.component2 import Counter2
from src.Gallery.gallery import Gallery
from page import childComponent


  # Multiple component add under main component
@component
def MainComponent():
    
    return html.div(
        Counter1(), Counter2(), childComponent(), Gallery()
        ) 