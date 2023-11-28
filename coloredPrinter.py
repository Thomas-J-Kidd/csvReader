
class ColoredPrinter:
    COLORS = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }

    OPTIONS = {
        'bold': '\033[1m',
        'underline': '\033[4m',
    }
    
                      # currently not used. Todo: make titles and stuff
    FORMATTING = {
        'title': '#',

    }

    ENDC = '\033[0m'

    def print(self, text, color=None, options=None):
        
        if color not in self.COLORS:
            color = 'white'  # Default to white if color is not specified

        color_code = self.COLORS[color]
        options_code = ''.join([self.OPTIONS[opt] for opt in options]) if options else ''

        formatted_text = f"{color_code}{options_code}{text}{self.ENDC}"
        print(formatted_text)

        

