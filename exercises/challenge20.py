# Faça um programa em python que abra e reproduza o audio de um arquivo mp3

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(r'C:\Users\kelve\Desktop\PTYHON REVIEW\exercises\music\musiceduardo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
