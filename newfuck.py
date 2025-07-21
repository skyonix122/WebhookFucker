import requests
import time
import sys

def loading_screen(duration=3):
    print("Lade Tool ", end="")
    for _ in range(duration * 3):  # z.B. 3 Sekunden mit 3 Punkten pro Sekunde
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.33)
    print("\nFertig!\n")

def send_webhook_message(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("Nachricht gesendet!")
            return True
        else:
            print(f"Fehler: Statuscode {response.status_code}")
            return False
    except Exception as e:
        print(f"Fehler beim Senden: {e}")
        return False

def spam_webhook(webhook_url, message, amount):
    for i in range(amount):
        print(f"Sende Nachricht {i+1}/{amount}")
        success = send_webhook_message(webhook_url, message)
        if not success:
            print("Stoppe Spam wegen Fehler.")
            break
        time.sleep(1)  # 1 Sekunde Pause zwischen den Nachrichten (kannst du anpassen)

def main():
    skull_art = r"""
                     :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
"""
    print(skull_art)
    loading_screen()

    webhook_url = input("Gib deine Discord Webhook URL ein: ").strip()
    message = input("Gib die Nachricht ein, die du senden möchtest: ").strip()
    amount = int(input("Wie oft soll die Nachricht gesendet werden? (Spam-Anzahl): ").strip())

    spam_webhook(webhook_url, message, amount)

if __name__ == "__main__":
    main()

