#ex021 - Faça um programa que abra e reproduza um audio de arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('welcome.mp3')
pygame.mixer.music.play()
pygame.event.wait()
