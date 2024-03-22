import Bunjee
import Kitpvp
import Mainhub
import Survival
import time
urlbunjee = "https://panel.magmanode.com/auth/login"
urlSur = "https://panel.magmanode.com/auth/login"
urlHub = "https://panel.magmanode.com/auth/login"
urlKit = "https://panel.magmanode.com/auth/login"
def main():
    while True:

        Bunjee.open_chrome_incognito(urlbunjee)
        print("1st server started")
        time.sleep(1)
        Mainhub.open_chrome_incognito(urlHub)
        print("Hub Started")
        time.sleep(1)
        Survival.open_chrome_incognito(urlSur)
        print("Survival Started")
        time.sleep(1)
        Kitpvp.open_chrome_incognito(urlKit)
        print("Kitpvp started")
        time.sleep(30 * 60)


if __name__ == "__main__":
    main()