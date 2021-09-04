from twitchobserver import Observer
import pyttsx3

# for the tts
engine = pyttsx3.init()
channel = "pawngrubber"

with Observer("username", "Oauth") as observer:
    observer.join_channel(channel)
    print("Joined channel", channel)
    print("Press Ctrl+C to quit, you might have to close the terminal window sometimes.")

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':
                    message = event.message
                    print(message)
                    
                    # TODO get list of mods instead of hard-coding mod usernames
                    mods = ["thefuxia", "smarterchess", "streamlabs", "grubberbot", "lalizig", "paradajzcity",
                    "duellinksguy", "thewretch2", "vietd", "poitaoforpresident", "chesscomchris", "mynameislegyon", "f0rgetaboutit",
                    "zuname", "rakshakthetall", "drittman13", "expired_febreeze", "strance_02", "marko_sreck", "flyingseverus"]
                    
                    if event.nickname in mods:
                        if "!tts" in message:
                            text = message.lstrip("!tts")
                            engine.say(text)
                            engine.runAndWait()
                        
        except KeyboardInterrupt:
            observer.leave_channel(channel)
            observer.stop()
            quit()
