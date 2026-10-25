import time #cuma make 1 libary yaitu time

DELAY_HURUF = 0.1 #BEBAS MAU DI ATUR BERAPA
DELAY_BARIS = 1 #BEBAS MAU DI ATUR BERAPA

LYRICS = [
" ",
" ",     #BEBAS MAU KALIAN ISI APA LIRIK NYA
" ",
]
#main
def main():
    for line in LYRICS:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(DELAY_HURUF)
        print()
        time.sleep(DELAY_BARIS)
  
if __name__=="__main__":
    main()
