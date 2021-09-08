import sys
import os

from deep_translator import GoogleTranslator
from sys import platform

if platform == "win32":
	os.system("cls")
   else:
	os.system("clear")

print("    Basic translator  ")
print(" ")
print(" Discord: Enough#7502")
print(" GitHub: github.com/Enoughsdv")
print(" ")
print(" #Enter the language you want to translate this text")

target = input(" Language: ").lower()

print(" ")
print(" #Enter the text to be translated")

text_translate = input(" Text: ")

translated = GoogleTranslator(source="auto", target=target).translate(text_translate)

if platform == "win32":
	os.system("cls")
   else:
	os.system("clear")

print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
print(" ")
print(f" Target: {target}")
print(f" Text to be translated: {text_translate}")
print(" ")
print(" ")
print(f" Result: {translated}")
print(" Mode: Google translator")
print(" ")
print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
