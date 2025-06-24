#USER ACCOUNT SYSTEM
import datetime
import time
class User:
    def __init__(self, username, password, secret_answer):
        self.username = username
        self.__password = password
        self._login_attempts = 0
        self._account_locked = False
        self._secret_answer = secret_answer
        self._last_password_change = datetime.datetime.now()
        self._last_login = datetime.datetime.now()
        self._login_history = []
        self._lock_time = None

    def _validate_password(self, pd):
        return (len(pd) >= 8 and 
        any(c.isdigit() for c in pd) and
        any(c.isupper() for c in pd)
        )
    def update_password(self, new_pd):
        if self._validate_password(new_pd):
            self.__password = new_pd
            self._last_password_change = datetime.datetime.now()
            self.__log("Password updated.")
            print(f"Password is updated successfully")
        else:    
            print(f"Passsword is too weak.")
        
    def show_username(self):
        print(self.username)
    def __log(self, msg):
        with open ("log.txt", "a") as f:
            f.write(f"{self.username} -> {msg}\n")

    def login(self, pd):
        self._login_history.append((datetime.datetime.now(), pd == self.__password))
        if self._account_locked:
            if self.reset_state():
                print("Account was locked but is now unlocked.You can try it again.")
            else:
                print("Account is locked. Please wait at least one minute.")
                return False
            return False
        if self.__password == pd:
            self._login_attempts = 0
            self._last_login = datetime.datetime.now()
            self.__log("Login successful.")
            print("Successful login")
            return True
        else:
            self._login_attempts += 1
            self.__log("Login failed.")
            print("Incorrect password")
            if self._login_attempts >= 3:
                self._account_locked = True
                self._lock_time = datetime.datetime.now()
                print("Account is locked due to too many failed attempts.Wait at least one minute.")
            return False
    def change_username(self, new_username):
        self.username = new_username
        self.__log("Username changed")
    def reset_password(self, answer, new_password):
        if answer == self._secret_answer:
            if self._validate_password(new_password):
                self.__password = new_password
                self.__log("Password reseted")
                print("Password reseted successfully")
            else:
                print("Password is not valid")
        else:
            self.__log("Secret keyword is not correct")
            print("Failed attempt to reset password")
    def get_last_login_time(self):
        print(self._last_login)
    def show_login_history(self):
        for time, status in self._login_history:
            print(f"{time} -> {'Success' if status else 'Fail'}")
    def reset_state(self):
        if self._lock_time is None:
            return False
        time_now = datetime.datetime.now()
        if (time_now - self._lock_time).total_seconds() >= 60:
            self._account_locked = False
            self._login_attempts = 0
            self._lock_time = None
            return True
        return False
    
user = User("johndoe321", "mypassword", "eod")
while True:
    print("\n1. Login\n2. Update Password\n3. Reset Password\n4. Show Login History\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        pd = input("Enter your password: ")
        user.login(pd)
    elif choice == '2':
        new_pd = input("Enter new password: ")
        user.update_password(new_pd)
    elif choice == '3':
        answer = input("Enter your secret answer: ")
        new_pd = input("Enter new password: ")
        user.reset_password(answer, new_pd)
    elif choice == '4':
        user.show_login_history()
    elif choice == '5':
        break
    else:
        print("Invalid option")
