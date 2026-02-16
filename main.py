from grille import *
import time

pygame.init()
grille = Board()
grille.preparation_niveau()
grille.afficher_terminal()

slide_sound = pygame.mixer.Sound("./sound/slide_sound.wav")
level_sound = pygame.mixer.Sound("./sound/level_sound.wav")
slide_sound.set_volume(0.1)
level_sound.set_volume(0.3)

w = 900
h= 800
stride_x= 100
stride_y = 100
screen = pygame.display.set_mode((w, h))
bg_img = pygame.image.load("./img/board_img.jpg")
bg_img = pygame.transform.scale(bg_img, (w, h))
font = pygame.font.SysFont(None, 32)
textLevelImg = font.render('NIVEAU:'+ str(grille.level+1), True, (255,255,255))
textLevelRect = textLevelImg.get_rect()
textLevelRect.center = (800,250)
textClearImg= font.render('NIVEAU FINIE!', True, (0,255,0),(0,0,255))
textClearRect = textClearImg.get_rect()
textClearRect.center = (w//2, h//2)

running = True
sel_voiture = ""
nivFinie = False
time_levUp = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not nivFinie:
                if event.key == K_a:
                    sel_voiture = "a"
                elif event.key == K_b:
                    sel_voiture = "b"
                elif event.key == K_c:
                    sel_voiture = "c"
                elif event.key == K_d:
                    sel_voiture = "d"
                elif event.key == K_e:
                    sel_voiture = "e"
                elif event.key == K_f:
                    sel_voiture = "f"
                elif event.key == K_g:
                    sel_voiture = "g"
                elif event.key == K_h:
                    sel_voiture = "h"
                elif event.key == K_i:
                    sel_voiture = "i"
                elif event.key == K_j:
                    sel_voiture = "j"
                elif event.key == K_k:
                    sel_voiture = "k"
                elif event.key == K_o:
                    sel_voiture = "o"
                elif event.key == K_p:
                    sel_voiture = "p"
                elif event.key == K_q:
                    sel_voiture = "q"
                elif event.key == K_r:
                    sel_voiture = "r"
                elif event.key == K_x:
                    sel_voiture = "x"
                
                # Déplacements de la voiture
                elif event.key == pygame.K_LEFT:
                    if grille.isOnboard(sel_voiture):
                        if grille.voitures[sel_voiture].direction == 'h':
                            if grille.deplace_voiture(sel_voiture, -1):
                                pygame.mixer.Sound.play(slide_sound)
                elif event.key == pygame.K_RIGHT:
                    if grille.isOnboard(sel_voiture):
                        if grille.voitures[sel_voiture].direction == 'h':
                            if grille.deplace_voiture(sel_voiture, 1):
                                pygame.mixer.Sound.play(slide_sound)
                elif event.key == pygame.K_UP:
                    if grille.isOnboard(sel_voiture):
                        if grille.voitures[sel_voiture].direction == 'v':
                            if grille.deplace_voiture(sel_voiture, -1):
                                pygame.mixer.Sound.play(slide_sound)
                elif event.key == pygame.K_DOWN:
                    if grille.isOnboard(sel_voiture):
                        if grille.voitures[sel_voiture].direction == 'v':
                            if grille.deplace_voiture(sel_voiture, 1):
                                pygame.mixer.Sound.play(slide_sound)

    # Affichage de l'état de la grille et des voitures
    screen.blit(bg_img, (0, 0))
    for v in grille.voitures:
        curr_v = grille.voitures[v]
        screen.blit(curr_v.image, (curr_v.posi[0] * stride_x + 100, curr_v.posi[1] * stride_y + 100))
    
    textLevelImg = font.render('NIVEAU: ' + str(grille.level + 1), True, (255, 255, 255))
    screen.blit(textLevelImg, textLevelRect)
    pygame.display.update()
    
    # Vérification du niveau terminé
    if nivFinie == False:
        nivFinie = grille.isLevelCleared()
    
    time_levUp = pygame.time.get_ticks()
    if nivFinie:
        pygame.mixer.Sound.play(level_sound)
        screen.blit(textClearImg, textClearRect)
        pygame.display.update()
        while pygame.time.get_ticks() - time_levUp < 4000:
            continue
        
        grille.level += 1
        nivFinie = False
        grille.preparation_niveau()
        
    pygame.display.update()
pygame.quit()