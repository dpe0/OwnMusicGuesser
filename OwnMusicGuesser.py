try: 
    savegaming = open('OwnMusicGuesser.txt', 'x')
    savegaming.close()
except: pass
savegaming = open('OwnMusicGuesser.txt', 'r')
maxscore=savegaming.read()
#print(maxscore)
savegaming.close()

win,lplusratio,winstreakmax =0,0,0
idkman2021,start,avgtime,fcount,finalscore,averagestuff,winstreak,keepmalding,L,mold,moldy,ablibibabium=0,0,[],0,0,0,0,0,False,[],0,0
import random, os, vlc, ffmpeg, time, math
def big_chungus(what):
    global sound, idkman2021, win, lplusratio, start,avgtime, fcount,finalscore, L,maxscore,averagestuff, winstreak,winstreakmax,keepmalding,mold,moldy,ablibibabium
    if what==0 or what==1:
        if what==0:
            if fcount<=int(amount.get()): keepmalding=fcount
            else: keepmalding=int(amount.get())
            ablibibabium=math.ceil(float(keepmalding)/10)
            window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=int(100/ablibibabium))
            amount.grid_remove()
            title.grid_remove()
            folderbutton.grid_remove()
            window.minsize(1000, 100)
            bababooey=tk.Label(text='Right:\nWrong:', justify='left')
            bababooey.grid(row=1, column=9, sticky='w')
            bababooey=tk.Label(text='Current score\nCurrent max score:', justify='left')
            bababooey.grid(row=4, column=9, sticky='w')
            bababooey=tk.Label(text='Last guess:\nAvg guess:', justify='left')
            bababooey.grid(row=2, column=9, sticky='w')
            bababooey=tk.Label(text='Current streak:    \nMax streak:   ', justify='left')
            bababooey.grid(row=3, column=9, sticky='w')
            finalscocurrectnscorered=tk.Label(text='0       \n0     ', justify='left')
            finalscocurrectnscorered.grid(row=4, column=10, sticky='w')
            score = tk.Label(text='0        \n0       ', justify='left')
            score.grid(row=1, column=10, sticky='w')
            stunlock = tk.Label(text='0     \n0     ', justify='left')
            stunlock.grid(row=3, column=10, sticky='w')
            # eject the sussy amongus from impostor
            if folder=='':
                import sys as sus
                sus.exit()
            if idkman2021==1:
                sound.stop()
                win,lplusratio,avgtime,finalscore=0,0,[],0
                lastguess=tk.Label(text='               \n              ', justify='left')
                lastguess.grid(row=2, column=10, sticky='w')
            for i in range(min(int(keepmalding),10)):window.rowconfigure(i, minsize=50, pad=2)
        # creates a list of SONGS
        global songs
        songs=['']*int(keepmalding)
        a=0
        b=0
        for i in range(int(keepmalding)):
            while not (songs[i].lower().endswith(('.mp3','.wav', '.flac', '.aac', '.ogg', '.wma', '.pcm', '.aiff', '.alac', '.dsd')) or a>100):
                songs[i]=random.choice(os.listdir(folder))
                a+=1
                #print('a',a)
                #print(songs[i] in songs[:i]+songs[i+1:])
                #print(songs[:i]+songs[i+1:])
                #print(not(songs[i] in songs[:i]+songs[i+1:]))
                #print(not ((songs[i] in songs[:i]+songs[i+1:]) or b>100))
                while ((songs[i] in songs[:i]+songs[i+1:]) and b<100): 
                    songs[i]=random.choice(os.listdir(folder))
                    b+=1
                    #print('b',b)
        #print(songs)
        global chosen
        chosen=random.choice(songs)
        big_chungus(2)
    else:
        idkman2021=1
        choice=[tk.Button]*int(keepmalding)
        for i in range(int(keepmalding)):
            if len(songs[i])>(120-ablibibabium*4)/ablibibabium: choice[i] = tk.Button(text=songs[i][:int((120-ablibibabium*4)/ablibibabium)],command=lambda x=songs[i]: big_chungus(x), bg='grey90')
            else: choice[i] = tk.Button(text=songs[i],command=lambda x=songs[i]: big_chungus(x), bg='grey90')
            choice[i].grid(row=(i%10)+1, column=int(9/ablibibabium)*math.floor(i/10), columnspan=int(9/ablibibabium), sticky="we", padx=10)
        #print(choice)
        #print(what)
        #print(chosen)
        if what==2:
            #print (folder+'/'+chosen)
            #print(ffmpeg.probe(folder+'/'+chosen)['format']['duration'])
            sound = vlc.MediaPlayer()
            amongus=vlc.Media(folder+'/'+chosen)
            amongus.add_option('start-time='+str(random.randrange(int(float((ffmpeg.probe(folder+'/'+chosen)['format']['duration'])))-20)))
            sound.set_media(amongus)
            sound.play()
            start = time.time()
        elif what==chosen:
            win+=1
            #lastguess = tk.Label(text='Last guess:\n' + str(round((time.time()-start),2)) +' s')
            #lastguess.grid(row=2, column=9, sticky='we')
            if L==False: 
                avgtime.append(time.time()-start)
                mold.append(time.time()-start)
            else: mold=[]
            L=False
            averagestuff=sum(avgtime)/max(len(avgtime),1)
            moldy=sum(mold)/max(len(mold),1)
            #scoreavg = tk.Label(text='Average guess time:\n' + str(round(averagestuff,2)) +' s')
            #scoreavg.grid(row=3, column=9, sticky='we')
            winstreak+=1
            winstreakmax=max(winstreak, winstreakmax)
            currectnscore=max((fcount**0.5)*(win/((lplusratio+1)))*(1/max(moldy**2, 1))*((int(keepmalding)/2)**1.4), (fcount**0.5)*winstreak*(1/max(moldy**2, 1))*((int(keepmalding)/4)**2))
            #finalscocurrectnscorered=tk.Label(text='Current score:\n' + str(round(currectnscore)))
            #finalscocurrectnscorered.grid(row=4, column=9, sticky='we')
            finalscore=max(finalscore,currectnscore)
            #finalscored=tk.Label(text='Current maximum score:\n' + str(round(finalscore)), font=("Arial 10 bold"))
            #finalscored.grid(row=5, column=9, sticky='we')
            maxscore=max(float(finalscore),float(maxscore))
            finalsmaxscorecored=tk.Label(text='Top score:       \n' + str(round(float(maxscore)))+'     ', justify='left')
            finalsmaxscorecored.grid(row=20, column=9, sticky='w')
            #qwqq
            lastguess=tk.Label(text=str(round((time.time()-start),2)) +' s      \n'+str(round(averagestuff,2)) +' s     ', justify='left')
            lastguess.grid(row=2, column=10, sticky='w')
            finalscocurrectnscorered=tk.Label(text=str(round(currectnscore))+'      \n'+str(round(finalscore))+'        ', justify='left')
            finalscocurrectnscorered.grid(row=4, column=10, sticky='w')
            score = tk.Label(text=str(win)+'        \n'+str(lplusratio)+'       ', justify='left')
            score.grid(row=1, column=10, sticky='w')
            stunlock = tk.Label(text=str(winstreak)+'       \n'+str(winstreakmax)+'     ', justify='left')
            stunlock.grid(row=3, column=10, sticky='w')

            #score.grid_remove()
            sound.stop()
            #print('thats right!!!') 
            for i in range(int(keepmalding)):
                choice[i].grid_remove()
            big_chungus(1)
        else:
            #score.grid_remove()
            #print('L + ratio') 
            lplusratio+=1
            winstreak=0
            score = tk.Label(text=str(win)+'\n'+str(lplusratio), justify='left')
            score.grid(row=1, column=10, sticky='w')
            currectnscore=max((fcount**0.5)*(win/((lplusratio+1)))*(1/max(moldy**2, 1))*((int(keepmalding)/4)**2), (fcount**0.5)*winstreak*(1/max(moldy**2, 1))*((int(keepmalding)/4)**2))
            finalscocurrectnscorered=tk.Label(text=str(round(currectnscore))+'\n'+str(round(finalscore)), justify='left')
            finalscocurrectnscorered.grid(row=4, column=10, sticky='w')
            stunlock = tk.Label(text=str(winstreak)+'\n'+str(winstreakmax), justify='left')
            stunlock.grid(row=3, column=10, sticky='w')
            L=True




#ask for  afolder 
def folderget():
    a=0
    global folder, fcount
    folder=  tk.filedialog.askdirectory ()
    foldertext = tk.Label(text=folder +' - ')
    foldertext.grid(row=20, column=1, sticky="ew") #nasty stuff
    a=1

    #start the epic gaming
    start = tk.Button(
        text="Begin",
        command=lambda: big_chungus(0)
    )
    start.grid(row=20, column=0, sticky="w", pady=5, padx=10)
    fcount=len([entry for entry in os.listdir(folder) if (os.path.isfile(os.path.join(folder, entry)) and entry.lower().endswith(('.mp3','.wav', '.flac', '.aac', '.ogg', '.wma', '.pcm', '.aiff', '.alac', '.dsd')))])
    count = tk.Label(text=str(fcount)+' songs')
    count.grid(row=20, column=2, sticky='we')

import tkinter.filedialog
from tkinter import ttk
import tkinter as tk

window=tk.Tk()
#window.maxsize(1200, 1200)
window.title('Own Music Guesser')
window.tk.call('tk', 'scaling', 2.0)


#ask for flder 
title = tk.Label(text="Music Guesser", font=("Arial", 15))
title.grid(row=0, column=0, columnspan=10, sticky="we", pady=10)

folderbutton = tk.Button(
    text="Select folder",
    command=folderget
)
folderbutton.grid(row=1, column=0, columnspan=9, sticky="we", pady=5, padx=10)

#amount of sonsgs
amount = tk.Entry()
amount.insert(0, "5")
amount.grid(row=2, column=0, sticky="we", pady=5, padx=10, columnspan=9)
title = tk.Label(text="Difficulty")
title.grid(row=2, column=9, sticky="w")
try: 
    tmp=float(maxscore)
    tmp=float(finalscore)
except: 
    maxscore=0
    finalscore=0
fifafofufe=tk.Label(text='Top score:\n' + str(int(max(float(maxscore), float(finalscore)))))
fifafofufe.grid(row=20, column=9, sticky='we')

window.mainloop()
savegaming = open('OwnMusicGuesser.txt', 'w+')
savegaming.write(str(max(float(maxscore), float(finalscore))))
savegaming.close()
