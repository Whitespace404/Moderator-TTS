from twitchobserver import Observer
import pyttsx3

engine = pyttsx3.init()
channel = "pawngrubber"

with Observer("<username, maybe use grubberbot>", "<get oath key here: https://twitchapps.com/tmi/>") as observer:
    observer.join_channel(channel)
    print("Joined channel", channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':
                    message = event.message
                    print(message)
                    
                    mods = observer.list_moderators(channel)
                    
                    if event.nickname in mods:
                        if "!announce" in message:
                            text = message.lstrip("!announce")
                            engine.say(text)
                            engine.runAndWait()
                        
        except KeyboardInterrupt:
            observer.leave_channel(channel)
            quit()
