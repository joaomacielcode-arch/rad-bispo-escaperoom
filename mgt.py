import pygame
from pygame import mouse
import bts
from timer import Timer
import numpy as np

screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('escaperoom')
clock = pygame.time.Clock()
pygame.mixer.init()

pygame.font.init()
text_font = pygame.font.SysFont("Arial", 35)
scary_font = pygame.font.SysFont("Felix Titling", 45)
bunda_font = pygame.font.SysFont("Comic Sans MS", 28)
bunda_font_small = pygame.font.SysFont("Comic Sans MS", 19)

run = True

#definindo imagens
bg = pygame.image.load('imgs/fundo.png').convert_alpha()
bg2 = pygame.image.load('imgs/fundo2.png').convert_alpha()
bau = pygame.image.load('imgs/baut.png').convert_alpha()
jan = pygame.image.load('imgs/janelat.png').convert_alpha()
jan_txt = pygame.image.load('imgs/barratxr.png').convert_alpha()
pap = pygame.image.load('imgs/papelt.png').convert_alpha()
seta = pygame.image.load('imgs/mvsetat.png').convert_alpha()
seta2 = pygame.image.load('imgs/mvsetat2.png').convert_alpha()
chave = pygame.image.load('imgs/chavet.png').convert_alpha()
bauopen = pygame.image.load('imgs/bauopent.png').convert_alpha()
portaferro = pygame.image.load('imgs/portaferro.png').convert_alpha()
botao = pygame.image.load('imgs/botaot.png').convert_alpha()
botaopreto = pygame.image.load('imgs/botaopt.png').convert_alpha()
botalua = pygame.image.load('imgs/botalua.png').convert_alpha()
botarde = pygame.image.load('imgs/botarde.png').convert_alpha()
botasol = pygame.image.load('imgs/botasun.png').convert_alpha()
botaclip = pygame.image.load('imgs/botaclip.png').convert_alpha()
ferroopen = pygame.image.load('imgs/portaferroopent.png').convert_alpha()
telapr = pygame.image.load('imgs/telapreta.png').convert_alpha()
fall = pygame.image.load('imgs/fall.gif').convert_alpha()

#imgs2
portaferro2 = pygame.image.load('imgs2/portaferro2.png').convert_alpha()
bg3 = pygame.image.load('imgs2/fundo3.png').convert_alpha()
prat = pygame.image.load('imgs2/prateleira.png').convert_alpha()
bgesq = pygame.image.load('imgs2/fundoesq.png').convert_alpha()
bgdir = pygame.image.load('imgs2/fundodir.png').convert_alpha()
vivario = pygame.image.load('imgs2/vivariocobra.png').convert_alpha()
postit = pygame.image.load('imgs2/postit.png').convert_alpha()
peconha = pygame.image.load('imgs2/peconha.png').convert_alpha()
maqtopera = pygame.image.load('imgs2/whackamole.png').convert_alpha()
botaotoupe = pygame.image.load('imgs2/botaotoupe.png').convert_alpha()
toupeira = pygame.image.load('imgs2/toupe.png').convert_alpha()
joazinho = pygame.image.load('imgs2/joazinho.png').convert_alpha()
mesajoao = pygame.image.load('imgs2/mesajoao.png').convert_alpha()
joaofala = pygame.image.load('imgs2/joaofala.png').convert_alpha()
balaofala = pygame.image.load('imgs2/balaofala.png').convert_alpha()
luzdesligada = pygame.image.load('imgs2/luzdesligada.png').convert_alpha()
luzligada1 = pygame.image.load('imgs2/luzligada1.png').convert_alpha()
luzligada2 = pygame.image.load('imgs2/luzligada2.png').convert_alpha()
luzligada3 = pygame.image.load('imgs2/luzligada3.png').convert_alpha()
okbutton = pygame.image.load('imgs2/okbutton.png').convert_alpha()
abutton = pygame.image.load('imgs2/abutton.png').convert_alpha()
bbutton = pygame.image.load('imgs2/bbutton.png').convert_alpha()
cbutton = pygame.image.load('imgs2/cbutton.png').convert_alpha()
xbutton = pygame.image.load('imgs2/xbutton.png').convert_alpha()
joaomorto = pygame.image.load('imgs2/joaomorto.png').convert_alpha()
chavejoao = pygame.image.load('imgs2/chavejoao.png').convert_alpha()
whackplaca = pygame.image.load('imgs2/whackplaca.png').convert_alpha()
botaotoupedeslig = pygame.image.load('imgs2/botaotoupedeslig.png').convert_alpha()
chavetoupe = pygame.image.load('imgs2/chavetoupe.png').convert_alpha()
livroantidoto = pygame.image.load('imgs2/livroantidoto.png').convert_alpha()
paginaintro = pygame.image.load('imgs2/paginatut.png').convert_alpha()
pagina1 = pygame.image.load('imgs2/pagina1.png').convert_alpha()
pagina2 = pygame.image.load('imgs2/pagina2.png').convert_alpha()
pagina3 = pygame.image.load('imgs2/pagina3.png').convert_alpha()
pagina4 = pygame.image.load('imgs2/pagina4.png').convert_alpha()
pagina5 = pygame.image.load('imgs2/pagina5.png').convert_alpha()
pagina6 = pygame.image.load('imgs2/pagina6.png').convert_alpha()
botaopassar = pygame.image.load('imgs2/botaopassar.png').convert_alpha()
leitorcobra = pygame.image.load('imgs2/leitorcobra.png').convert_alpha()
chavecobra = pygame.image.load('imgs2/cobrakey.png').convert_alpha()
joguemeusjogos = pygame.image.load('imgs2/joguemeusjogos.png').convert_alpha()
papeljoguejogos = pygame.image.load('imgs2/papeljoguejogos2.png').convert_alpha()
setabaixo = pygame.image.load('imgs2/setabaixo.png').convert_alpha()
portaferro2open = pygame.image.load('imgs2/portaferro2open.png').convert_alpha()
botaopross = pygame.image.load('imgs2/botaopross.png').convert_alpha()
brahma = pygame.image.load('imgs2/brahma.png').convert_alpha()
cena1 = pygame.image.load('imgs2/cenadorme.png').convert_alpha()
cena2 = pygame.image.load('imgs2/cenaacorda.png').convert_alpha()
cena3 = pygame.image.load('imgs2/cenareclama.png').convert_alpha()
cena4 = pygame.image.load('imgs2/cenadormednv.png').convert_alpha()
cena5 = pygame.image.load('imgs2/cenadormednv2.png').convert_alpha()
cena6 = pygame.image.load('imgs2/cenasombra1.png').convert_alpha()
cena7 = pygame.image.load('imgs2/cenasombra2.png').convert_alpha()
interruptor = pygame.image.load('imgs2/interruptor.png').convert_alpha()

#definindo botoes
bau_bt = bts.Button(300, 160, bau, 1)
jan_bt = bts.Button(0, 40, jan, 1)
pap_bt = bts.Button(160,250, pap, 1)
seta_bt = bts.Button(530,200, seta, 1)
seta2_bt = bts.Button(10,200,seta2,1)
ch_bt = bts.Button(350,280,chave,1)
ch_op = bts.Button(304,105,bauopen,1)
pt_fr = bts.Button(320,33,portaferro,1)
bt_vr = bts.Button(262, 111,botao,1)
bt_pr = bts.Button(266,117,botaopreto,1)
bt_lua = bts.Button(170, 100,botalua,1)
bt_tr = bts.Button(200,100,botarde,1)
bt_sol = bts.Button(170, 130,botasol,1)
bt_clip = bts.Button(200, 130,botaclip,1)
fr_op = bts.Button(320, 33, ferroopen, 1)

#definindo botoes 2
bt_ptf2 = bts.Button(232,102,portaferro2,1)
bt_cbr = bts.Button(192,96,vivario,1)
bt_pst = bts.Button(280,208,postit,1)
bt_pec = bts.Button(438,151,peconha,1)
bt_toup = bts.Button(196,129,maqtopera,1)
bt_maqt = bts.Button(80,130,botaotoupe,0.75)
bt_joao = bts.Button(419, 87, joazinho,1)
ok_bt = bts.Button(334,149,okbutton,1.3)
a_bt = bts.Button(24,96,abutton,1)
b_bt = bts.Button(24, 131, bbutton,1)
c_bt = bts.Button(24, 165, cbutton, 1)
chave_j = bts.Button(437, 233, chavejoao,1)
b_wplaca = bts.Button(275,129,whackplaca,1)
bt_tpoff = bts.Button(80,130,botaotoupedeslig,0.75)
bt_chtoup = bts.Button(288,230,chavetoupe,1)
bt_livroa = bts.Button(60,109,livroantidoto,1)
x_bt = bts.Button(563,2,xbutton,1)
x_bt2 = bts.Button(563,309,xbutton,1)
x_bt3 = bts.Button(480,3,xbutton,1)
bt_passdi = bts.Button(574,149,botaopassar,1)
bt_passes = bts.Button(2,149,botaopassar,1)
bt_ltrcobra = bts.Button(90,120,leitorcobra,1)
bt_chcobra = bts.Button(93,324,chavecobra,1)
bt_joguejogos = bts.Button(400, 329, joguemeusjogos,1)
seta3_bt = bts.Button(270,348,setabaixo,1)
bt_ptf2op = bts.Button(232,102,portaferro2open,1)
bt_pross = bts.Button(240,360,botaopross,1)
bt_inter = bts.Button(67,0,interruptor,1)

#posicoes toupeira
bt_digg1 = bts.Button(217,167,toupeira,1)
bt_digg2 = bts.Button(336,167,toupeira,1)
bt_digg3 = bts.Button(310,203,toupeira,1)
bt_digg4 = bts.Button(238,203,toupeira,1)
bt_digg5 = bts.Button(274,227,toupeira,1)

#Efeitos Sonoros
sfx_bau = pygame.mixer.Sound('sfx/bauabrindor.mp3')
sfx_papel = pygame.mixer.Sound('sfx/papelsom.mp3')
sfx_botao = pygame.mixer.Sound('sfx/botaosom.mp3')
sfx_ferro = pygame.mixer.Sound('sfx/ferroabre.mp3')
sfx_erro = pygame.mixer.Sound('sfx/wrongr.mp3')
sfx_acerto = pygame.mixer.Sound('sfx/acerto.mp3')
sfx_chave = pygame.mixer.Sound('sfx/chavegetr.mp3')
sfx_queda = pygame.mixer.Sound('sfx/willhelm.mp3')
sfx_bonk = pygame.mixer.Sound('sfx/bonk.mp3')

#Função de escrever texto
def textu(text,font,text_col,x,y):
    img = font.render(text,True, text_col)
    screen.blit(img,(x,y))

def toggle_var():
    global varto
    global seq
    varto = not varto
    seq = np.random.randint(5)

#Timers
txt_time = Timer(2500, repeat=False)
timer_3 = Timer(3000, repeat=False)
tmr_toupmini = Timer(24000, repeat=False)
timer_toup2 = Timer(1200, repeat=True, func=toggle_var)
timer_toupw = Timer(1500, repeat=False)
timer_MORTE = Timer(480000,repeat=False)

#Variáveis de Interação
action_var = ''
sala_var = 'sala1'

#Variáveis Trocáveis
key_get = False
bau_open = False
bt_get = False
cod_ok = False
joao_falando = False
falaon = False
reading = False
joaowin = False
toupwin = False
cobrawin = False
toupkey_get = False
joaokey_get = False
cobrakey_get = False
toupmini_on = False
mortestart = False
livroaberto = False

#endgame
Morte = False

#puzzle1
resposta = [1,1,3,3]
cod_input = []

#topeira
varto = False
seq = None
pontos = 0

#cobra
coding = False
codtxt = ''
codresposta = 'bb22x'

#minigames vencidos
wins = []

#CODIGO SECRETO LEGAL PARA PEGAR INPUT DO JOGADOR
#for event in pygame.event.get():
               # if event.type == pygame.KEYDOWN:
                  #  testetxt += event.unicode

while run:
    txt_time.update()
    ci_size = len(cod_input)

    #Sala 1
    if sala_var == 'sala1':
        screen.blit(bg,(0,0))

        if txt_time.active and action_var == 'bau':
            screen.blit(jan_txt,(3,320))
            textu("Um baú trancado.", text_font, (255,255,255), 10,333)
        
        if bau_open == False:
            if bau_bt.draw(screen):
                if key_get == False:
                    action_var = 'bau'
                    txt_time.activate()
                    print('Bau')
                    print(bau_open)
                    print(key_get)
                elif key_get == True:
                    sfx_bau.play()
                    bau_open = True

        if txt_time.active and action_var == 'bauaberto':
            screen.blit(jan_txt,(3,320))
            screen.blit(botao, (512,340))
            textu("Eu abri o baú e consegui um botão.", text_font, (255,255,255), 10,333)

        if bau_open == True:
            if ch_op.draw(screen):
                action_var = 'bauaberto'
                txt_time.activate()
                print('Aberto')


        if txt_time.active and action_var == 'janela':
            screen.blit(jan_txt,(3,320))
            textu("Uma janela. Está escuro lá fora.", text_font, (255,255,255), 10,333)

        if jan_bt.draw(screen):
            action_var = 'janela'
            txt_time.activate()
            print('Janela')

        if txt_time.active and action_var == 'papel':
            screen.blit(jan_txt,(3,320))
            textu("A nota diz: '2x Horário Atual, 2x o Inverso'.", text_font, (255,255,255), 10,333)

        if pap_bt.draw(screen):
            sfx_papel.play()
            action_var = 'papel'
            txt_time.activate()
            print('Papel')

        if seta_bt.draw(screen):
            sala_var = 'sala2'
            print('Mover')
            pygame.time.wait(400)

    #Sala 2
    if sala_var == 'sala2':
        txt_time.update()
        screen.blit(bg2,(0,0))

        if txt_time.active and action_var == 'chave':
            screen.blit(jan_txt,(3,320))
            textu("Uma chave... talvez seja útil.", text_font, (255,255,255), 10,333)

        if key_get == False:
            if ch_bt.draw(screen):
                sfx_chave.play()
                action_var = 'chave'
                txt_time.activate()
                print('Chave')
                key_get = True

        if seta2_bt.draw(screen):
            sala_var = 'sala1'
            print('Mover')
            pygame.time.wait(400)

        if txt_time.active and action_var == 'portaferro':
            screen.blit(jan_txt,(3,320))
            textu("Uma porta de ferro. Trancada.", text_font, (255,255,255), 10, 333)

        if cod_ok == False:
            if pt_fr.draw(screen):
                action_var = 'portaferro'
                txt_time.activate()
                print('Fechada')

        if txt_time.active and action_var == 'botaop':
            screen.blit(jan_txt,(3,320))
            textu("Um espaço para um botão... onde acho um?", text_font, (255,255,255), 10, 333)

        if bt_get == False:
            if bt_pr.draw(screen):
                if bau_open ==  False:
                    action_var = 'botaop'
                    txt_time.activate()
                    print('Botao')
                elif bau_open:
                    bt_get = True

        if txt_time.active and action_var ==  'botaov':
            screen.blit(jan_txt,(3,320))
            textu("Eu coloquei o botão no espaço.", text_font, (255,255,255), 10, 333)

        if bt_get == True:
            if bt_vr.draw(screen):
                action_var = 'botaov'
                txt_time.activate()
                print(cod_input)
                print(ci_size)
                if ci_size >= 4:
                    if cod_input == resposta:
                        sfx_ferro.play()
                        cod_ok = True
                        print('Correto!')
                    elif cod_input != resposta:
                        sfx_erro.play()
                        cod_input.clear()
                        print('Errado!')
        
        #Botões Tempo
        if bt_lua.draw(screen):
            sfx_botao.play()
            cod_input.append(1)
            print('Lua')
        
        if bt_tr.draw(screen):
            sfx_botao.play()
            cod_input.append(2)
            print('Tarde')

        if bt_sol.draw(screen):
            sfx_botao.play()
            cod_input.append(3)
            print('Sol')
        
        if bt_clip.draw(screen):
            sfx_botao.play()
            cod_input.append(4)
            print('Eclipse')

        if cod_ok == True:
            if fr_op.draw(screen):
                sala_var = 'fimdemo'
                action_var = 'txt1'
                print('Porta Aberta')
                timer_3.activate()

    if sala_var == 'fimdemo':
        screen.blit(telapr,(0,0))
        txt_time.update()
        timer_3.update()

        if not timer_3.active and action_var == 'txt1':
            textu("...", text_font, (255,255,255), 288,150)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txt2'
        
        if not timer_3.active and action_var == 'txt2':
            textu("Que estranho...", text_font, (255,255,255), 202,170)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txt3'
        
        if not timer_3.active and action_var == 'txt3':
            textu("Você sente como se...", text_font, (255,255,255), 160,170)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txt4'
        
        if not timer_3.active and action_var == 'txt4':
            textu("Seus pés não tocassem", scary_font, (255,255,255), 25,160)
            textu("O Chão", scary_font, (255,255,255), 210,200)
            if bt_pross.draw(screen):
                sfx_queda.play()
                timer_3.activate()
                action_var = 'txt5'

        if not timer_3.active and action_var == 'txt5':
            textu("...", scary_font, (255,255,255), 286,160)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txt6'
        
        if not timer_3.active and action_var == 'txt6':
            textu("Que frio...", scary_font, (255,255,255), 167,160)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txt7'
        
        if not timer_3.active and action_var == 'txt7':
            if bt_inter.draw(screen):
                sfx_botao.play()
                sala_var = 'fundo1'
                mortestart = True
                timer_MORTE.activate()

    if not timer_MORTE.active and mortestart == True:
        sala_var = 'morte'

    if sala_var == 'morte':
        timer_3.update()
        screen.blit(telapr,(0,0))
        if Morte == False:
            if bt_pross.draw(screen):
                action_var = 'txtm1'
                timer_3.activate()
                Morte = True

        if not timer_3.active and action_var == 'txtm1':
            textu("...", scary_font, (255,255,255), 288,250)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txtm2'
                print('press')
        
        if not timer_3.active and action_var == 'txtm2':
            textu("Uma dor aguda", scary_font, (255,255,255), 100,130)
            textu("Fura seu peito.", scary_font, (255,255,255), 120,170)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'txtm3'
        
        if not timer_3.active and action_var == 'txtm3':
            textu("VOCÊ MORREU", scary_font, (255,0,0), 131,150)
            if bt_pross.draw(screen):
                run =  False


    if sala_var == 'fundo1':
        timer_MORTE.update()
        txt_time.update()
        screen.blit(bg3,(0,0))

        if coding == False and reading == False:
            if seta_bt.draw(screen):
                sala_var = 'fundodir'
                print('Mover')
                pygame.time.wait(400)

            if seta2_bt.draw(screen):
                sala_var = 'fundoesq'
                print('Mover')
                pygame.time.wait(500)
            
            if seta3_bt.draw(screen):
                sala_var = 'fundotras'
                pygame.time.wait(500)
        
        if len(wins) == 0:
            screen.blit(luzdesligada,(210,36))
        
        if len(wins) == 1:
            screen.blit(luzligada1,(210,36))

        if len(wins) == 2:
            screen.blit(luzligada2,(210,36))
        
        if len(wins) == 3:
            if bt_ptf2op.draw(screen):
                mortestart = False
                sala_var = 'fimdojogo'
                action_var = 'fimtxt1'
                timer_3.activate()

            screen.blit(luzligada3,(210,36))

        if bt_ltrcobra.draw(screen):
            coding = True

        if bt_joguejogos.draw(screen):
            reading = True

        if txt_time.active and action_var == 'cobrawon':
            screen.blit(jan_txt,(3,320))
            textu("O leitor ejetou uma chave...", text_font, (255,255,255), 10,333)

        if cobrakey_get == False and cobrawin:
            if bt_chcobra.draw(screen):
                sfx_chave.play()
                txt_time.activate()
                action_var = 'cobrawon'
                cobrakey_get = True
                wins.append(2)
        
        if coding:
            screen.blit(jan_txt,(3,320))
            textu("Digite o código do antídoto:", text_font, (255,255,255), 10,333)
            textu(codtxt, text_font, (255,255,255), 365,333)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    codtxt += event.unicode
                    if len(codtxt) == 5:
                        if codtxt == codresposta:
                            coding = False
                            cobrawin = True
                            print('Correto!')
                        else:
                            codtxt = ''
                            print('Errado!')

            if x_bt2.draw(screen):
                coding = False
                codtxt = ''
        
        if len(wins) != 3:
            if bt_ptf2.draw(screen):
                print('porta')

        if reading:
            screen.blit(papeljoguejogos,(111,6))
            if x_bt3.draw(screen):
                reading = False

    if sala_var == 'fundoesq':
        txt_time.update()
        screen.blit(bgesq,(0,0))
        screen.blit(prat,(180,180))

        if livroaberto == False:

            if bt_livroa.draw(screen):
                action_var = 'paginatut'
                livroaberto =  True

            if txt_time.active and action_var == 'cobra':
                screen.blit(jan_txt,(3,320))
                textu("Uma cobra em um vivário desertico.", text_font, (255,255,255), 10,333)

            if bt_cbr.draw(screen):
                txt_time.activate()
                action_var = 'cobra'
                print('Vivario')

            if txt_time.active and action_var == 'postit':
                screen.blit(jan_txt,(3,320))
                textu("'OBS: SÓ ALIMENTAR COM INSETOS!!!'", text_font, (255,255,255), 10,333)

            if bt_pst.draw(screen):
                txt_time.activate()
                action_var = 'postit'
                print('Mensagem')

            if txt_time.active and action_var == 'peconha':
                screen.blit(jan_txt,(3,320))
                textu("Um pote com peçonha esverdeada.", text_font, (255,255,255), 10,333)

            if bt_pec.draw(screen):
                txt_time.activate()
                action_var = 'peconha'
                print('Peconha')
            
            if seta_bt.draw(screen):
                sala_var = 'fundo1'
                print('Mover')
                pygame.time.wait(400)
        
        elif livroaberto == True:
            if action_var == 'paginatut':
                screen.blit(paginaintro,(12,16))
                if bt_passdi.draw(screen):
                    action_var = 'pagina1'

            if action_var == 'pagina1':
                screen.blit(pagina1,(12,16))
                if bt_passdi.draw(screen):
                    action_var = 'pagina2'
                if bt_passes.draw(screen):
                    action_var = 'paginatut'
            
            if action_var == 'pagina2':
                screen.blit(pagina2,(12,16))
                if bt_passdi.draw(screen):
                    action_var = 'pagina3'
                if bt_passes.draw(screen):
                    action_var = 'pagina1'
            
            if action_var == 'pagina3':
                screen.blit(pagina3,(12,16))
                if bt_passdi.draw(screen):
                    action_var = 'pagina4'
                if bt_passes.draw(screen):
                    action_var = 'pagina2'

            if action_var == 'pagina4':
                screen.blit(pagina4,(12,16))
                if bt_passdi.draw(screen):
                    action_var = 'pagina5'
                if bt_passes.draw(screen):
                    action_var = 'pagina3'
            
            if action_var == 'pagina5':
                screen.blit(pagina5,(12,16))
                if bt_passdi.draw(screen):
                    action_var = 'pagina6'
                if bt_passes.draw(screen):
                    action_var = 'pagina4'
            
            if action_var == 'pagina6':
                screen.blit(pagina6,(12,16))
                if bt_passes.draw(screen):
                    action_var = 'pagina5'

            if x_bt.draw(screen):
                livroaberto = False

    if sala_var == 'fundotras':
        screen.blit(bg3,(0,0))
        txt_time.update()
        tmr_toupmini.update()
        timer_toupw.update()
        timer_toup2.update()

        if toupmini_on == False or toupkey_get:
            if seta3_bt.draw(screen):
                sala_var = 'fundo1'
                pygame.time.wait(500)

        if bt_toup.draw(screen):
            print('Maquina Toupeira')

        if txt_time.active and action_var == 'toupkey':
            screen.blit(jan_txt,(3,320))
            textu("Uma chave emergiu da máquina...", text_font, (255,255,255), 10,333)

        if txt_time.active and action_var == 'placatoup':
            screen.blit(jan_txt,(3,320))
            textu("'Bata na topeira! Chegue aos 35 pontos!'", text_font, (255,255,255), 10,333)

        if b_wplaca.draw(screen):
            txt_time.activate()
            action_var = 'placatoup'

        if bt_maqt.draw(screen) and toupmini_on == False:
            print('Botao Toupeira')
            tmr_toupmini.activate()
            timer_toup2.activate()
        
        if toupmini_on:
            if bt_tpoff.draw(screen):
                print('OFF')

        if tmr_toupmini.active:
            toupmini_on = True
            print(varto)
            print(pontos)
            if varto and timer_toup2.active:
                if seq == 0:
                    if bt_digg1.draw(screen):
                        sfx_bonk.play()
                        pontos += 1
                        print('toupy1')
                
                if seq == 1:
                    if bt_digg2.draw(screen):
                        sfx_bonk.play()
                        pontos += 1
                        print('toupy2')
                
                if seq == 2:
                    if bt_digg3.draw(screen):
                        sfx_bonk.play()
                        pontos += 1
                        print('toupy3')

                if seq == 3:
                    if bt_digg4.draw(screen):
                        sfx_bonk.play()
                        pontos += 1
                        print('toupy4')
                    
                if seq == 4:
                    if bt_digg5.draw(screen):
                        sfx_bonk.play()
                        pontos += 1
                        print('toupy5')
            else:
                print('ola')

        if not tmr_toupmini.active:
            if pontos >= 35:
                if toupkey_get == False:
                    if bt_chtoup.draw(screen):
                        txt_time.activate()
                        sfx_chave.play()
                        action_var = 'toupkey'
                        toupkey_get = True
                        print('ola')
                        wins.append(1)
            
            else:
                toupmini_on = False
                pontos = 0

    if sala_var == 'fundodir':
        txt_time.update()
        screen.blit(bgdir,(0,0))
        screen.blit(mesajoao,(400,213))

        if seta2_bt.draw(screen):
            falaon = False
            joao_falando =  False
            sala_var = 'fundo1'
            print('Mover')
            pygame.time.wait(500)

        if txt_time.active and 'joaokeyget':
            screen.blit(jan_txt,(3,320))
            textu("Embaixo do boneco havia uma chave...", text_font, (255,255,255), 10,333)

        if joaokey_get == False and joaowin:
            if chave_j.draw(screen):
                sfx_chave.play()
                wins.append(3)
                joaokey_get = True
                action_var = 'joaokeyget'
                txt_time.activate()


        if falaon == True and joaowin == False:
            screen.blit(balaofala,(13,24))
            if action_var == 'joaozinho':
                textu("Responda minhas charadas", bunda_font, (0,0,0), 34, 50)
                textu("E vença meu jogo!", bunda_font, (0,0,0), 93, 85)
                textu(":D", bunda_font, (0,0,0), 190, 126)
                if ok_bt.draw(screen):
                    action_var = 'charada1'
                    print('Pressionado')
            screen.blit(joaofala,(419,87))
            if action_var == 'charada1':
                textu("O que é o que é: Tem coroa, mas não é rei.", bunda_font_small, (0,0,0), 20, 35)
                textu("É amarelo, mas não é de ouro?", bunda_font_small, (0,0,0), 21, 59)

                textu("ABACAXI", bunda_font_small, (255,0,0), 54, 94)
                textu("MARACUJÁ", bunda_font_small, (255,0,0), 54, 128)
                textu("MAÇÃ INDIANA", bunda_font_small, (255,0,0), 54, 164)
                
                if a_bt.draw(screen):
                    action_var = 'charada2'
                    print('A')
                if b_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('B')
                if c_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('C')
            
            if action_var == 'charada2':
                textu("O que um corvo e uma escrivaninha...", bunda_font_small, (0,0,0), 20, 35)
                textu("possuem em comum?", bunda_font_small, (0,0,0), 21, 59)

                textu("NADA", bunda_font_small, (255,0,0), 54, 94)
                textu("TUDO", bunda_font_small, (255,0,0), 54, 129)
                textu("NÃO FAÇO IDEIA", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('A')
                if b_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('B')
                if c_bt.draw(screen):
                    action_var = 'charada3'
                    print('C')
            
            if action_var == 'charada3':
                textu("Qual a cor da cobra, de suas pintas...", bunda_font_small, (0,0,0), 20, 35)
                textu("e de seus olhos, respectivamente?", bunda_font_small, (0,0,0), 21, 59)

                textu("AMARELO, PRETO, AZUL", bunda_font_small, (0,255,0), 54, 94)
                textu("AZUL, PRETO, AMARELO", bunda_font_small, (255,255,0), 54, 129)
                textu("LILÁS, VERDE, AMARELO", bunda_font_small, (255,0,255), 54, 164)

                if a_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('A')
                if b_bt.draw(screen):
                    action_var = 'charada4'
                    print('B')
                if c_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('C')
            
            if action_var == 'charada4':
                textu("O que não tem pulmões, mas precisa de ar;", bunda_font_small, (0,0,0), 20, 25)
                textu("não é vivo, mas cresce; fumaça...", bunda_font_small, (0,0,0), 21, 45)
                textu("mas não é chaminé?", bunda_font_small, (0,0,0), 21, 65)

                textu("MEU AMIGO JOSÉ", bunda_font_small, (255,0,0), 54, 94)
                textu("USINA DE PETRÓLEO", bunda_font_small, (255,0,0), 54, 129)
                textu("FOGO", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('A')
                if b_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('B')
                if c_bt.draw(screen):
                    action_var = 'charada5'
                    print('C')
            
            if action_var == 'charada5':
                textu("Qual a cor do céu lá fora?", bunda_font_small, (0,0,0), 84, 47)

                textu("CARMESIM", bunda_font_small, (255,0,0), 54, 94)
                textu("ESCURO", bunda_font_small, (255,0,0), 54, 129)
                textu("CLARO", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('A')
                if b_bt.draw(screen):
                    action_var = 'charada6'
                    print('B')
                if c_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('C')

            if action_var == 'charada6':
                textu("Qual o número dessa charada...", bunda_font_small, (0,0,0), 20, 35)
                textu("Somado a 10, menos 2?", bunda_font_small, (0,0,0), 21, 59)

                textu("14", bunda_font_small, (255,0,0), 54, 94)
                textu("13", bunda_font_small, (255,0,0), 54, 129)
                textu("12", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    action_var = 'charada7'
                    print('A')
                if b_bt.draw(screen):
                    falaon = False
                    joao_falando =  False
                    print('B')
                if c_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('C')
            
            if action_var == 'charada7':
                textu("Em uma escala de 1 à 10... qual nota", bunda_font_small, (0,0,0), 20, 35)
                textu("Você daria para este jogo?", bunda_font_small, (0,0,0), 21, 59)

                textu("ZERO", bunda_font_small, (255,0,0), 54, 94)
                textu("DEZ", bunda_font_small, (255,0,0), 54, 129)
                textu("ALGO ENTRE ZERO E DEZ", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('A')
                if b_bt.draw(screen):
                    action_var = 'charada8'
                    print('B')
                if c_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    print('C')
            
            if action_var ==  'charada8':
                textu("Entre estas três opções... qual sua", bunda_font_small, (0,0,0), 20, 35)
                textu("Fruta favorita?", bunda_font_small, (0,0,0), 21, 59)

                textu("MAÇÃ INDIANA", bunda_font_small, (255,0,0), 54, 94)
                textu("ABACAXI", bunda_font_small, (255,0,0), 54, 129)
                textu("MARACUJÁ", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    action_var = 'charada9'
                    print('A')
                if b_bt.draw(screen):
                    action_var = 'charada9'
                    print('B')
                if c_bt.draw(screen):
                    action_var = 'charada9'
                    print('C')
            
            if action_var == 'charada9':
                textu("Você está perdendo seu tempo?", bunda_font_small, (0,0,0), 68, 55)

                textu("SIM", bunda_font_small, (255,0,0), 54, 94)
                textu("NÃO", bunda_font_small, (255,0,0), 54, 129)
                textu("NÃO FAÇO IDEIA", bunda_font_small, (255,0,0), 54, 164)

                if a_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    joaowin = True
                    print('A')
                if b_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    joaowin = True
                    print('B')
                if c_bt.draw(screen):
                    falaon = False
                    joao_falando = False
                    joaowin = True
                    print('C')

        if joao_falando == False:
            if bt_joao.draw(screen):
                joao_falando = True
                falaon = True
                action_var = 'joaozinho'

        if joao_falando == False and joaowin == True:
            screen.blit(joaomorto,(419,87))

    if sala_var == 'fimdojogo':
        screen.blit(telapr,(0,0))
        txt_time.update()
        timer_3.update()

        if not timer_3.active and action_var == 'fimtxt1':
            textu("...", text_font, (255,255,255), 289,170)
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'fimtxt2'
        
        if not timer_3.active and action_var == 'fimtxt2':
            screen.blit(cena1,(0,0))
            if bt_pross.draw(screen):
                action_var = 'fimtxt3'
        
        if action_var == 'fimtxt3':
            screen.blit(cena2,(0,0))
            textu("UAAAAAAAAAAAAAAAAH!!!!!!", text_font, (255,255,0), 90,20)
            if bt_pross.draw(screen):
                action_var = 'fimtxt4'
        
        if action_var == 'fimtxt4':
            screen.blit(cena3,(0,0))
            textu("Urgh... foi tudo...", text_font, (255,255,0), 24,12)
            textu("Um sonho...?", text_font, (255,255,0), 24,47)
            if bt_pross.draw(screen):
                action_var = 'fimtxt5'
        
        if action_var == 'fimtxt5':
            screen.blit(cena4,(0,0))
            textu("Que merda, hein...", text_font, (255,255,0), 24,12)
            if bt_pross.draw(screen):
                action_var = 'fimtxt6'
        
        if action_var == 'fimtxt6':
            screen.blit(cena5,(0,0))
            if bt_pross.draw(screen):
                action_var = 'fimtxt7'
        
        if action_var == 'fimtxt7':
            screen.blit(cena6,(0,0))
            if bt_pross.draw(screen):
                timer_3.activate()
                action_var = 'fimtxt8'
        
        if timer_3.active and action_var == 'fimtxt8':
            screen.blit(cena6)
        
        if not timer_3.active and action_var == 'fimtxt8':
            screen.blit(cena7,(0,0))
            txt_time.activate()
            action_var = 'fim'

        if not txt_time.active and action_var == 'fim':
            run = False

    #Código pra fechar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
    clock.tick(60)
pygame.quit()