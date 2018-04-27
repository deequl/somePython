from pyfiglet import Figlet

f = Figlet(font='slant')
render_to_render = input("Enter text to transform: ")
print( f.renderText(render_to_render))