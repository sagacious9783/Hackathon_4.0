import speak
speak.ap("Switched off")
subprocess.call("amixer set Master mute",shell=True)
