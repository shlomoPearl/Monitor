import math
import os
import time
from datetime import datetime
from cryptography.fernet import Fernet
import AutoGui
import ManualGui

name_service_list = 'serviceList.txt'
name_service_change = 'statusLog.txt'
operation_sys = os.name
WIDTH = 1024
HEIGHT = 720


class Monitor:
    def __init__(self):
        self.t = self.get_time()
        self.event1 = None
        self.event2 = None
        self.run = True
        self.key = None
        # self.fernet = None

    def decrypt(self, file_name):
        # using the key

        fernet = Fernet(self.key)

        # opening the encrypted file
        with open(file_name, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(file_name, 'wb') as dec_file:
            dec_file.write(decrypted)

    def encrypt(self, file_name):
        # key generation
        self.key = Fernet.generate_key()

        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(self.key)

        # opening the key
        with open('filekey.key', 'rb') as filekey:
            self.key = filekey.read()

        # using the generated key
        fernet = Fernet(self.key)

        # opening the original file to encrypt
        with open(file_name, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    # use in terminal to get services
    def write_linux_services(self, date_time):
        os.popen(f'echo {date_time} >> {name_service_list} | service --status-all | grep + >> {name_service_list}')
        self.encrypt(name_service_list)

    # use in terminal to get services
    def write_windows_services(self, date_time):
        os.popen(f'echo {date_time} >> {name_service_list}')
        os.popen(f'net start >> {name_service_list}')
        if self.key is not None:
            self.decrypt(name_service_list)
        time.sleep(1)
        self.encrypt(name_service_list)

    # use to insert the services into file on each time the use want
    def update_services_list(self):
        date_time = 'Date and Time ~ ' + str(datetime.now())
        if operation_sys == 'nt':
            self.write_windows_services(date_time)
        else:
            self.write_linux_services(date_time)

    # write new services that run now and old services that don't run now
    def write_change(self, new, old, current_time):
        if len(new) == 0 and len(old) == 0:
            return
        with open(name_service_change, 'a', encoding='utf-8') as f:
            f.write(f'changes from {current_time}:\n')
            if len(new) > 0:
                f.write('those services are new:\n')
                f.writelines(new)
            if len(old) > 0:
                f.write('those services stopped:\n')
                f.writelines(old)
            f.write('\n')
        f.close()
        self.encrypt(name_service_change)

    """
    this func get two lists of services and check the difference
    the flag is to know if is in manual or auto state
    """

    def check_status_log(self, last, new, flag):
        new_services = []
        old_services = []
        for new_serv in new:
            if new_serv not in last:  # it's a new service
                new_services.append(new_serv + '\n')
                print(f"this is a new service: {new_serv}")
        for old_serv in last:
            if old_serv not in new:  # this service doesn't run
                old_services.append(old_serv + '\n')
                print(f"this service stopped: {old_serv}")
        if flag:  # is in manual mode
            return
            # return new_services, old_services
        date_time = datetime.now()
        self.write_change(new_services, old_services, date_time)
        return

    """
    read the file and return the last list of services in this file
    """

    def get_last_log(self):
        list_log = []
        # ISO-8859-8 is for supported in hebrew
        self.decrypt(name_service_list)  # decrypt file and then read info
        time.sleep(1)
        with open(name_service_list, 'r', encoding='ISO-8859-8') as f:
            while True:
                try:
                    log = f.readline()
                    if not log:
                        break
                    if log.strip():
                        list_log.append(log.strip())
                # if decode failed
                except UnicodeDecodeError:
                    print("reading of one line get wrong")
        f.close()
        self.encrypt(name_service_list)
        real_index = 0
        for index, line in enumerate(list_log):
            if len(line.split('~')) > 1:
                real_index = index

        last_log = list_log[real_index + 1:]

        return last_log

    """
    get two dates in format: YYYY-MM-DD and return tha difference between them
    """

    def date_fiff(self, date1: str, date2: str):
        date1 = date1.split('-')
        date2 = date2.split('-')
        y_d = abs(int(date1[0]) - int(date2[0]))
        m_d = abs(int(date1[1]) - int(date2[1]))
        d_d = abs(int(date1[2]) - int(date2[2]))
        return y_d + m_d + d_d

    """
    get two times in format: HH-:MM:SS and return tha difference between them
    """

    def time_fiff(self, time1, time2):
        time1 = time1.split(':')
        time2 = time2.split(':')
        t1 = int(time1[0]) + (int(time1[1]) / 60) + (float(time1[2]) / 600)
        t2 = int(time2[0]) + (int(time2[1]) / 60) + (float(time2[2]) / 600)
        return abs(t1 - t2)

    # get date and time- event - and return the log in file which is closest to this event
    def get_log_by_event(self, event: tuple):
        date_diff = math.inf
        time_diff = math.inf
        index = 0
        self.decrypt(name_service_list)
        # time.sleep(1)
        with open(name_service_list, 'r', encoding='ISO-8859-8') as f:
            log_list = f.readlines()
            self.encrypt(name_service_list)
            for i, line in enumerate(log_list):
                if len(line.split('~')) > 1:
                    date = self.date_fiff(line.split('~')[1].strip().split(' ')[0], event[0])
                    time = self.time_fiff(line.split('~')[1].strip().split(' ')[1], event[1])
                    if date <= date_diff and time < time_diff:
                        date_diff = date
                        time_diff = time
                        index = i
            log_list = log_list[index + 1:]
            for i, line in enumerate(log_list):
                if len(line.split('~')) > 1:
                    index = i
                    break
            log_list = log_list[:index]
            return log_list

    # get two event and show the difference between them
    def manual(self):
        event = self.get_event()
        if event is not None:
            event1, event2 = event
            event1 = event1.split(' ')
            event1 = (event1[0], event1[1])
            event2 = event2.split(' ')
            event2 = (event2[0], event2[1])
            event1_list = self.get_log_by_event(event1)
            event2_list = self.get_log_by_event(event2)
            self.check_status_log(event1_list, event2_list, True)

    # run each time -t and check services changes
    def auto(self):
        self.update_services_list()
        time_factor = int(self.t)
        last_check = time.time()
        while True:
            current_time = time.time()
            if last_check <= current_time - time_factor:
                last_check += time_factor
                last_log = self.get_last_log()
                self.update_services_list()
                time.sleep(1)
                new_log = self.get_last_log()
                self.check_status_log(last_log, new_log, False)

    # gui window for scheduled the system
    def get_time(self):
        a = AutoGui.AutoGui()
        a.auto()
        t = a.t
        return t

    def get_event(self):
        manu = ManualGui.ManualGui()
        manu.manual()
        event = manu.event
        return event


if __name__ == '__main__':
    m = Monitor()
    # m.encrypht('ServiceList.txt')
    m.auto()
    # m.manual()

# example of event format
# "2022-03-20 21:50:00"
# "2022-03-20 21:54:50"
